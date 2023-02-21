import time
import subprocess
import psutil

class JobFactory():
    def __init__(self):
        self.file = ""
        self.length = int()
        self.interval = int()
        self.cmd = ""

    def set_cmd(self, **kargs):
        if kargs.get("job_name") == "make model":
            if not kargs.get("file") is None:
                self.file = kargs.get("file")
            if not kargs.get("length") is None:
                self.length = kargs.get("length")
            if not kargs.get("interval") is None:
                self.interval = kargs.get("interval")
            self.cmd = f"python {self.file} --length {self.length} --sleep {self.interval}"

class JobManager(JobFactory):
    def __init__(self):
        # self.file = ""
        # self.length = int()
        # self.interval = int()
        self.proc = ""
        self.proc_id = int()

    def set_job(self, **kargs):
        if not kargs.get("file") is None:
            self.file = kargs.get("file")
        if not kargs.get("length") is None:
            self.length = kargs.get("length")
        if not kargs.get("interval") is None:
            self.interval = kargs.get("interval")

    def run(self):
        cmd = f"python {self.file} --length {self.length} --sleep {self.interval}"
        proc = subprocess.Popen(cmd)
        self.proc = proc
        self.proc_id = proc.pid
        print("run:", self.proc_id)

    def kill(self):
        print("kill:", self.proc_id)
        # self.proc.kill()
        psutil.Process(self.proc_id).terminate()

    def is_finish(self):
        if self.proc.poll() is None: # 実行中
            return False
        else: # 終了
            return True

if __name__ == '__main__':
    job = JobManager()

    job.set_cmd(job_name="make model", file="test/job.py", length=5, interval=1)

    job.run()

    print(job.is_finish())

    time.sleep(3)
    # job.kill()

    time.sleep(3)
    print(job.is_finish())