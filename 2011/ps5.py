#!python2
# Tui Popenoe
# ps5.py - RSS Feed Filter

import feedparser
import string
import time
import re
from project_util import translate_html
from news_gui import Popup

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

class NewsStory(object):
    def __init__(self, guid='', title='', subject='', summary='', link=''):
        self.guid = guid
        self.title = title
        self.subject = subject
        self.summary = summary
        self.link = link

    def get_guid(self):
        return self.guid

    def get_title(self):
        return self.title

    def get_subject(self):
        return self.subject

    def get_summary(self):
        return self.summary

    def get_link(self):
        return self.link

class Trigger(object):
    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        raise NotImplementedError

class WordTrigger(Trigger):
    def __init__(self, word):
        self.word = word.lower()

    def is_word_in(self, text):
        if re.search(r'\b' + re.escape(self.word) + r'\b', text.lower()):
            return True
        else:
            return False

class TitleTrigger(WordTrigger):
    def evaluate(self, story):
        title = story.get_title().lower()
        if self.is_word_in(title):
            return True
        else:
            return False

class SubjectTrigger(WordTrigger):
    def evaluate(self, story):
        subject = story.get_subject().lower()
        if self.is_word_in(subject):
            return True
        else:
            return False

class SummaryTrigger(WordTrigger):
    def evaluate(self, story):
        summary = story.get_summary().lower()
        if self.is_word_in(summary):
            return True
        else:
            return False

class NotTrigger(Trigger):
    def __init__(self, T):
        self.T = T

    def evaluate(self, story):
        return not self.T.evaluate(story)

class AndTrigger(Trigger):
    def __init__(self, T1, T2):
        self.T1 = T1
        self.T2 = T2

    def evaluate(self, story):
        return self.T1.evaluate(story) and self.T2.evaluate(story)

class OrTrigger(Trigger):
    def __init__(self, T1, T2):
        self.T1 = T1
        self.T2 = T2

    def evaluate(self, story):
        return self.T1.evaluate(story) or self.T2.evaluate(story)

class PhraseTrigger(Trigger):
    def __init__(self, phrase):
        self.phrase = phrase

    def evaluate(self, story):
        if self.phrase in story.get_summary():
            return True
        elif self.phrase in story.get_subject():
            return True
        elif self.phrase in story.get_title():
            return True
        else:
            return False

def filter_stories(stories, triggerlist):
    """
    Takes in a list of NewsStory-s.
    Returns only those stories for whom
    a trigger in triggerlist fires.
    """
    output = []
    for i in stories:
        for j in triggerlist:
            if j.evaluate(i):
                output.append(i)
    return output

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

    triggers = {}
    output_triggers = []
    for line in lines:
        if line[1] == 'SUBJECT':
            triggers[line[0]] = SubjectTrigger(line[2])
        if line[1] == 'SUMMARY':
            triggers[line[0]] = SummaryTrigger(line[2])
        if line[1] == 'TITLE':
            triggers[line[0]] = TitleTrigger(line[2])
        if line[1] == 'PHRASE':
            triggers[line[0]] = PhraseTrigger(line[2:])
        if line[1] == 'AND':
            triggers[line[0]] = AndTrigger(line[2], line[3])
        if line[1] == 'OR':
            triggers[line[0]] = OrTrigger(line[2], line[3])
        if line[1] == 'NOT':
            triggers[line[0]] = NotTrigger(line[2], line[3])
        if line[0] == 'ADD':
            for i in line:
                output_triggers.append(triggers[i])
    return output_triggers
    
import thread

def main_thread(p):
    # A sample trigger list - you'll replace
    # this with something more configurable in Problem 11
    t1 = SubjectTrigger("Obama")
    t2 = SummaryTrigger("MIT")
    t3 = PhraseTrigger("Supreme Court")
    t4 = OrTrigger(t2, t3)
    triggerlist = [t1, t4]
    
    # TODO: Problem 11
    # After implementing readTriggerConfig, uncomment this line 
    #triggerlist = readTriggerConfig("triggers.txt")

    guidShown = []
    
    while True:
        print "Polling..."

        # Get stories from Google's Top Stories RSS news feed
        stories = process("http://news.google.com/?output=rss")
        # Get stories from Yahoo's Top Stories RSS news feed
        stories.extend(process("http://rss.news.yahoo.com/rss/topstories"))

        # Only select stories we're interested in
        stories = filter_stories(stories, triggerlist)
    
        # Don't print a story if we have already printed it before
        newstories = []
        for story in stories:
            if story.get_guid() not in guidShown:
                newstories.append(story)
        
        for story in newstories:
            guidShown.append(story.get_guid())
            p.newWindow(story)

        print "Sleeping..."
        time.sleep(SLEEPTIME)

SLEEPTIME = 60 #seconds -- how often we poll

if __name__ == '__main__':
    p = Popup()
    thread.start_new_thread(main_thread, (p,))
    p.start()
