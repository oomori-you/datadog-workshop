"""Example of integration between Fabric and Datadog.
"""

from __future__ import with_statement
from fabric.api import *
from fabric.colors import *
from dogapi.fab import setup, notify
import os

# 事前に export DATADOG_API_KEY=*** の用に環境変数にapi_keyを設定してください
setup(api_key = os.environ["DATADOG_API_KEY"])
env.warn_only=True
ab_command = "ab -n 10000000 -c 5 http://localhost/info.php"

# Make sure @notify is just below @task
@task
@notify
def test_notify():
  print(green("send datadog event"))

@task
@notify
def run_ab():
  local("nohup {0} > /dev/null 2>&1 &".format(ab_command));
  print(green("start ab"))

@task
@notify
def kill_ab():
  local(u"pkill -f '{0}' > /dev/null 2>&1 &".format(ab_command));
  print(red("kill ab"))
