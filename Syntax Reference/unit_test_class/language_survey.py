#!/usr/bin/env python3

from survey import AnonymouseSurvery

question = "Which languages did you first learn to speak?"
my_survey = AnonymouseSurvery(question)

my_survey.show_question()

while True:
  response = input("Language: ")
  if response == 'q':
    break
  my_survey.store_response(response)

my_survey.show_results()