import sys

from squad.demo_prepro import prepro
from basic.demo_cli import Demo


class AnswererHandler:
    def __init__(self):
        self.demo = Demo()

    def __call__(self, paragraph, question):
        pq_prepro = prepro(paragraph, question)
        return self.demo.run(pq_prepro)

if __name__ == "__main__":
    fin = sys.stdin
    question = fin.readline()
    paragraph = " ".join(fin.readlines())

    answerer = AnswererHandler()
    answer = answerer(paragraph, question)

    print("Answer: %s" % answer)
