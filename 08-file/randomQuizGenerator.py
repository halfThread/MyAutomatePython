#!/usr/bin/env python
# -*- coding:utf8 -*-

"""
@version: 
@author: lh
@license: Apache Licence 
@contact: liuhuan0672@gmail.com
@site: 
@software: PyCharm
@file: randomQuizGenerator.py
@time: 2017/7/14 11:17
"""

capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix', 'Arkansas': 'Little Rock',
            'California': 'Sacramento', 'Colorado': 'Denver', 'Connecticut': 'Hartford', 'Delaware': 'Dover',
            'Florida': 'Tallahassee', 'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise',
            'Illinois': 'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas': 'Topeka',
            'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine': 'Augusta', 'Maryland': 'Annapolis',
            'Massachusetts': 'Boston', 'Michigan': 'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson',
            'Missouri': 'Jefferson City',
            'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada': 'Carson City', 'New Hampshire': 'Concord',
            'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
            'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City', 'Oregon': 'Salem',
            'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence', 'South Carolina': 'Columbia',
            'South Dakota': 'Pierre', 'Tennessee': 'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City',
            'Vermont': 'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston',
            'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

capitalsItems = list(capitals.items())


def generate_paper():
    for quizNum in range(35):
        # 创建存储文件的目录
        directory = 'QuizAndAnswers'
        if not os.path.exists(directory):
            os.mkdir(directory)

        # 创建问题文件与答案文件
        quizFile = open('capitals_quiz%s.txt' % (quizNum + 1), 'w')
        answerKeyFile = open('capitals_quiz_answers%s.txt' % (quizNum + 1), 'w')

        # 创建文件的头部信息
        quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
        quizFile.write(('  ' * 20) + 'State Capitals Quiz (Form %s)' % (quizNum + 1))
        quizFile.write('\n\n')

        states = list(capitals.keys())
        random.shuffle(states)

        for questionNum in range(50):
            # 获取所有的答案
            correctAnswer = capitals[states[questionNum]]
            wrongAnswers = list(capitals.values())
            # 删除正确答案
            del wrongAnswers[wrongAnswers.index(correctAnswer)]
            wrongAnswers = random.sample(wrongAnswers, 3)

            answerOptions = wrongAnswers + [correctAnswer]
            random.shuffle(answerOptions)

            quizFile.write('%s. What is the capital of %s?\n' %
                           (questionNum + 1, states[questionNum]))
            for i in range(4):
                quizFile.write('    %s. %s\n' % ('ABCD'[i], answerOptions[i]))
            quizFile.write('\n')

            answerKeyFile.write('%s. %s\n' % (questionNum + 1, 'ABCD'[answerOptions.index(correctAnswer)]))

        quizFile.close()
        answerKeyFile.close()


if __name__ == '__main__':
    generate_paper()
