# 6.00.1x Problem Set 7
# RSS Feed Filter

import feedparser
import string
import time
from project_util import translate_html
from Tkinter import *


#-----------------------------------------------------------------------
#
# Problem Set 7

#======================
# Code for retrieving and parsing RSS feeds
# Do not change this code
#======================

def process(url):
    """
    Fetches news items from the rss url and parses them.
    Returns a list of NewsStory-s.
    """
    feed = feedparser.parse(url)
    entries = feed.entries
    ret = []
    for entry in entries:
        guid = entry.guid
        title = translate_html(entry.title)
        link = entry.link
        summary = translate_html(entry.summary)
        try:
            subject = translate_html(entry.tags[0]['term'])
        except AttributeError:
            subject = ""
        newsStory = NewsStory(guid, title, subject, summary, link)
        ret.append(newsStory)
    return ret
#======================

#======================
# Part 1
# Data structure design
#======================

# Problem 1

class  NewsStory(object):
    def __init__(self, guid, title,subject,summary,link):
        self.guid = guid
        self.title = title
        self.subject = subject
        self.summary=summary
        self.link=link

    def getGuid(self):
        return self.guid

    def getTitle(self):
        return self.title

    def getSubject(self):
        return self.subject

    def getSummary(self):
        return self.summary

    def getLink(self):
        return self.link

#======================
# Part 2
# Triggers
#======================

class Trigger(object):
    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        # raise NotImplementedError

# Whole Word Triggers
# Problems 2-5

class WordTrigger(Trigger):
        def __init__(self, word):
            self.word = word

        def isWordIn(self, text):
            nonpuncuatedtext = self.replacePunctuationWithSpace(text)
            stringList = nonpuncuatedtext.split(' ')
            wordLower = self.word.lower()
            for str in stringList:
                if wordLower == str:
                    return True
            return False

        def replacePunctuationWithSpace(self, text):
            replace_punctuation = string.maketrans(string.punctuation, ' '*len(string.punctuation))
            nonPunctuatedText = text.translate(replace_punctuation)
            return nonPunctuatedText.lower()

class TitleTrigger(WordTrigger):

    def evaluate(self, story):
        return self.isWordIn(story.getTitle())

class SubjectTrigger(WordTrigger):

    def evaluate(self, story):
        return self.isWordIn(story.getSubject())

class SummaryTrigger(WordTrigger):

    def evaluate(self, story):
        return self.isWordIn(story.getSummary())


# Composite Triggers
# Problems 6-8

class NotTrigger(Trigger):
    def __init__(self, trigger):
        self.trigger=trigger

    def evaluate(self, news):
        return not self.trigger.evaluate(news)

class AndTrigger(Trigger):
    def __init__(self,trigger1,trigger2):
        self.trigger1=trigger1
        self.trigger2 = trigger2

    def evaluate(self, news):
        return self.trigger1.evaluate(news) and self.trigger2.evaluate(news)

class OrTrigger(Trigger):
    def __init__(self,trigger1,trigger2):
         self.trigger1=trigger1
         self.trigger2 = trigger2

    def evaluate(self, news):
        return self.trigger1.evaluate(news) or self.trigger2.evaluate(news)

# Phrase Trigger
# Question 9

class PhraseTrigger(Trigger):
    def __init__(self, word):
        self.word = word

    def evaluate(self, story):
        if self.word in story.getTitle() or self.word in story.getSubject() or self.word in story.getSummary():
            return True
        else:
            return False

#======================
# Part 3
# Filtering
#======================

def filterStories(stories, triggerlist):
    """
    Takes in a list of NewsStory instances.

    Returns: a list of only the stories for which a trigger in triggerlist fires.
    """
    triggeredStories=[]
    for story in stories:
        for trigger in triggerlist:
            if trigger.evaluate(story):
                if story not in triggeredStories:
                    triggeredStories.append(story)
    return triggeredStories

    # TODO: Problem 10
    # This is a placeholder (we're just returning all the stories, with no filtering) 
    return stories

#======================
# Part 4
# User-Specified Triggers
#======================

def makeTrigger(triggerMap, triggerType, params, name):
    """
    Takes in a map of names to trigger instance, the type of trigger to make,
    and the list of parameters to the constructor, and adds a new trigger
    to the trigger map dictionary.

    triggerMap: dictionary with names as keys (strings) and triggers as values
    triggerType: string indicating the type of trigger to make (ex: "TITLE")
    params: list of strings with the inputs to the trigger constructor (ex: ["world"])
    name: a string representing the name of the new trigger (ex: "t1")

    Modifies triggerMap, adding a new key-value pair for this trigger.

    Returns a new instance of a trigger (ex: TitleTrigger, AndTrigger).
    """
    for i in range(0,len(params)):
        if params[i] in triggerMap:
            params[i] = triggerMap.get(params[i])

    trigger=None
    if triggerType == 'SUBJECT':
        trigger=SubjectTrigger(params[0])
    elif triggerType=='TITLE':
        trigger = TitleTrigger(params[0])
    elif triggerType == 'SUMMARY':
        trigger = SummaryTrigger(params[0])
    elif triggerType == 'AND':
        trigger = AndTrigger(params[0],params[1])
    elif triggerType == 'NOT':
        trigger = NotTrigger(params[0])
    elif triggerType == 'OR':
        trigger = OrTrigger(params[0],params[1])
    elif triggerType == 'PHRASE':
        phraseStr=""
        for str in params:
            phraseStr = phraseStr+" "+str
        trigger = PhraseTrigger(phraseStr.strip())
    if trigger == None:
        raise NameError("trigger "+triggerType+" not found")
    triggerMap[name]= trigger;
    return trigger

def readTriggerConfig(filename):
    """
    Returns a list of trigger objects
    that correspond to the rules set
    in the file filename
    """

    # Here's some code that we give you
    # to read in the file and eliminate
    # blank lines and comments
    triggerfile = open(filename, "r")
    all = [ line.rstrip() for line in triggerfile.readlines() ]
    lines = []
    for line in all:
        if len(line) == 0 or line[0] == '#':
            continue
        lines.append(line)

    triggers = []
    triggerMap = {}

    # Be sure you understand this code - we've written it for you,
    # but it's code you should be able to write yourself
    for line in lines:

        linesplit = line.split(" ")

        # Making a new trigger
        if linesplit[0] != "ADD":
            trigger = makeTrigger(triggerMap, linesplit[1],
                                  linesplit[2:], linesplit[0])

        # Add the triggers to the list
        else:
            for name in linesplit[1:]:
                triggers.append(triggerMap[name])

    return triggers

print readTriggerConfig("triggers.txt")

import thread

SLEEPTIME = 60 #seconds -- how often we poll


def main_thread(master):
    # A sample trigger list - you'll replace
    # this with something more configurable in Problem 11
    try:
        # These will probably generate a few hits...
        t1 = TitleTrigger("Obama")
        t2 = SubjectTrigger("Romney")
        t3 = PhraseTrigger("Election")
        t4 = OrTrigger(t2, t3)
        triggerlist = [t1, t4]
        
        # TODO: Problem 11
        # After implementing makeTrigger, uncomment the line below:
        triggerlist = readTriggerConfig("triggers.txt")

        # **** from here down is about drawing ****
        frame = Frame(master)
        frame.pack(side=BOTTOM)
        scrollbar = Scrollbar(master)
        scrollbar.pack(side=RIGHT,fill=Y)
        
        t = "Google & Yahoo Top News"
        title = StringVar()
        title.set(t)
        ttl = Label(master, textvariable=title, font=("Helvetica", 18))
        ttl.pack(side=TOP)
        cont = Text(master, font=("Helvetica",14), yscrollcommand=scrollbar.set)
        cont.pack(side=BOTTOM)
        cont.tag_config("title", justify='center')
        button = Button(frame, text="Exit", command=root.destroy)
        button.pack(side=BOTTOM)

        # Gather stories
        guidShown = []
        def get_cont(newstory):
            if newstory.getGuid() not in guidShown:
                cont.insert(END, newstory.getTitle()+"\n", "title")
                cont.insert(END, "\n---------------------------------------------------------------\n", "title")
                cont.insert(END, newstory.getSummary())
                cont.insert(END, "\n*********************************************************************\n", "title")
                guidShown.append(newstory.getGuid())

        while True:

            print "Polling . . .",
            # Get stories from Google's Top Stories RSS news feed
            stories = process("http://news.google.com/?output=rss")

            # Get stories from Yahoo's Top Stories RSS news feed
            stories.extend(process("http://rss.news.yahoo.com/rss/topstories"))

            # Process the stories
            stories = filterStories(stories, triggerlist)

            map(get_cont, stories)
            scrollbar.config(command=cont.yview)


            print "Sleeping..."
            time.sleep(SLEEPTIME)

    except Exception as e:
        print e


# if __name__ == '__main__':
#
#     root = Tk()
#     root.title("Some RSS parser")
#     thread.start_new_thread(main_thread, (root,))
#     root.mainloop()

