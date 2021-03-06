# coding=utf-8
import gevent.monkey; gevent.monkey.patch_all()
from twisted.internet import reactor
from ultron.cluster.work.work_engine import WorkEngine

if __name__ == "__main__":
    reactor.__init__()
    work_engine = WorkEngine()
    reactor.run()
