"""
This program helps grade students' deliveries in Devilry 3, when using the
option labeled:    "Download Assignment"

This file should be placed in the directory containing the downloaded and
extracted folder; it should be called something like "in1900.2018h.weekX"

Run this program in Python 3 to get started – available commands are:

Y - Pass
N - Fail
R - Rerun Script
C - Comment
Q - Quit

To be able to run this program

    [1]     Set variable "main_folder" equal to a string with the name of the
    extracted folder.

    [2]     Set variable "files_to_run" equal to a list of strings, where each
    string is the name of one of the files you wish to grade.
"""

import os, re, datetime, sys
from subprocess import Popen, PIPE, call, STDOUT

#USER OPTIONS

main_folder = "in1900.2018h.week2"
files_to_run = ["ball_table2.py", "ball_table3.py", "sum_while.py", "population_table.py"]

#AUTOMATIC CONFIG

now = datetime.datetime.now()
date = now.strftime("%Y-%m-%d")
main_path = os.path.dirname(os.path.abspath(__file__))
main_path = re.sub(r"~(.*)", r"$HOME\1", main_path) + "/" + main_folder
longest_filename = len(max(files_to_run, key=len))

class Student(object):

    def __init__(self, path):
        self.student_folder = re.sub(r".*/([\w\d\-\.]+)", r"\1", path)
        self.username = re.sub(r"group-(\w+) -.*", r"\1", self.student_folder)
        dir = os.listdir("{}/{}"\
        .format(globals()['main_folder'], self.student_folder))[0]
        #self.rootpath = "{}/{}/delivery/".format(path, dir)
        self.rootpath = "{}/{}/".format(path, dir)
        #self.relpath = "{}/{}/{}/delivery"\
        self.relpath = "{}/{}/{}"\
        .format(globals()["main_folder"], self.student_folder, dir)
        self.deadline = re.sub(r"deadline(\d{4}-\d{2}-\d{2}) .*", r"\1", dir)
        self.present = self.check_files_present()
        self.missing = self.str_missing_files()
        self.success = None
        self.comment = {}


    def test_scripts(self):
        clear()
        txt =  "TESTING SCRIPTS FOR USER " + '\x1b[1;34;01m' + self.username +\
        '\x1b[0m' + "\n"
        txt += "Successful? (Y/N/R/S/C/Q)\n"
        txt += "YES-NO-RERUN-SOURCE-QUIT\n"
        print(txt)
        self.success = {}
        for k,v in self.present.items():
            if v is True:
                runstr = "Running " + '\x1b[1;34;01m' + \
                "{:{length}}".format(k, length = longest_filename) + \
                '\x1b[0m'
                txt += "\n" + runstr
                print(runstr, end = "")
                sys.stdout.flush()
                output = "\n\nExpected Output:\n"
                output += self.get_output_str(k).strip()
                print(output)
                runscript = True
                comments = 0
                while True:
                    if runscript is True:
                        self.run_script(k)
                    runscript = True
                    ans = get_key_press(allowed = "ynrscq")
                    if ans in ["y", "n"]:
                        break
                    elif ans == "s":
                        Popen(['gedit', "{}/{}".format(self.relpath, k)], stdin=open(os.devnull, 'r'))
                        runscript = False
                    elif ans == "c":
                        if comments == 0:
                            self.comment[k] = ""
                            input_str = "\nEnter a Comment:\n<1>"
                            print(input_str)
                            self.comment[k] += "\n<1>\n\t" + input("\t")
                        else:
                            input_str = "\nAdd Another Comment:\n<{}>"\
                            .format(comments + 1)
                            print(input_str)
                            self.comment[k] += "\n<{}>\n\t"\
                            .format(comments + 1) + input("\t")
                        comments += 1
                        runscript = False
                        clear()
                        print(txt, output)
                    elif ans == "q":
                        print('\x1b[1;31;01m' + '\nPROGRAM TERMINATED' + '\x1b[0m')
                        sys.exit(0)
                clear()
                print(txt, end = "")
                sys.stdout.flush()
                if ans == "y":
                    self.success[k] = True
                    confirm = '\x1b[1;32;01m' + '  OK' + '\x1b[0m'
                    txt += confirm
                    print(confirm)
                elif ans == "n":
                    self.success[k] = False
                    deny = '\x1b[1;31;01m' + '  FAILED' + '\x1b[0m'
                    txt += deny
                    print(deny)
                else:
                    raise ValueError("Invalid Selection")

    def get_output_str(self, filename):
        with open("{}/{}".format(self.relpath, filename), "r") as f:
            txt = f.read()
        pattern = re.compile(r"(['\"])\1\1(.*?)\1{3}", re.DOTALL)
        try:
            output = '\x1b[1;34;01m' + re.findall(pattern, txt)[-1][-1] + '\x1b[0m'
        except:
            output = '\x1b[1;31;01m' + 'EMPTY' + '\x1b[0m'
        return output

    def run_script(self, name):
        cmds = [
        "python3 {}".format(name),
        "read -p ~~~~~~~~~~~~~~~~~~~~~~~~~~~~DONE~~~~~~~~~~~~~~~~~~~~~~~~~~~~",
        "exit 0"]
        s = call("gnome-terminal --working-directory=\"{}\" -e 'bash -c \"{} exec bash\"'"\
        .format(self.rootpath + "/", ';'.join(cmds)), shell = True)

    def check_files_present(self):
        files = os.listdir(self.relpath)
        present = {}
        for f in globals()['files_to_run']:
            if f in files:
                present[f] = True
            else:
                present[f] = False
        return present

    def str_missing_files(self):
        txt = ""
        for k,v in self.present.items():
            if v is False:
                txt += "\n\t  " + '\x1b[1;31;01m' + k + '\x1b[0m'
        if txt == "":
            txt = "\nFILES     " + '\x1b[1;32;01m' + 'ALL DELIVERED' + '\x1b[0m'
        else:
            txt = "\nFILES     " + '\x1b[1;31;01m' + 'MISSING' + '\x1b[0m' + txt
        return txt

    def str_successful_files(self):
        success = "SUCCESS"
        failed = "FAILED"
        for k,v in self.success.items():
            if v is True:
                success += "\n\t  " + '\x1b[1;32;01m' + k + '\x1b[0m'
            else:
                failed += "\n\t  " + '\x1b[1;31;01m' + k + '\x1b[0m'
        txt = ""
        if success != "SUCCESS":
            txt += success
        if failed != "FAILED":
            if success != "SUCCESS":
                txt += "\n"
            txt += failed
        return txt

    def save(self, filename = None):
        savedir = "results_{}".format(globals()["main_folder"])

        if filename is None:
            filename = "{}_score.txt".format(self.username)

        lines = ["DEADLINE  {:<10}".format(self.deadline)]

        missing = "MISSING FILES"
        success = "SUCCESSFUL SCRIPTS"
        failed = "FAILED SCRIPTS"

        for k,v in self.present.items():
            if v is False:
                missing += "\n\t  " + k
        for k,v in self.success.items():
            if v is True:
                success += "\n\t  " + k
            else:
                failed += "\n\t  " + k

        if missing != "MISSING FILES":
            lines.append("\n\n" + missing)
        if success != "SUCCESSFUL SCRIPTS":
            lines.append("\n\n" + success)
        if failed != "FAILED SCRIPTS":
            lines.append("\n\n" + failed)
        for k,v in self.comment.items():
            lines.append("\n\n" + k + " COMMENTS:\n" + v)

        if savedir not in os.listdir():
            os.system("mkdir {}".format(savedir))
        with open(savedir + "/" + filename, "w+") as f:
            f.writelines(lines)

    def __str__(self):
        txt =  "USERNAME  " + '\x1b[1;34;01m' + self.username + '\x1b[0m'
        txt += "\nDEADLINE  {:<10}".format(self.deadline)
        txt += self.missing
        if self.success is not None:
            txt += "\n" + self.str_successful_files()
        return txt

    def __repr__(self):
        return self.__str__()

def clear(errorMsg = False):
    os.system('clear')

def get_key_press(allowed = 'all', caseSensitive = False):
    os.system("stty raw -echo")
    if allowed == 'all':
        key = sys.stdin.read(1)
        if caseSensitive is False:
            key = key.lower()
        os.system("stty -raw echo")
        return key
    elif allowed == 'letters':
        allowed = list(string.ascii_lowercase)
    elif allowed == 'numbers':
        allowed = [0,1,2,3,4,5,6,7,8,9]
    elif allowed == 'ynrscq':
        allowed = ['y','n','r','s','c','q']
    elif allowed == 'yn':
        allowed = ['y','n']
    while True:
        key = sys.stdin.read(1)
        if caseSensitive is False:
            key = key.lower()
        if isinstance(allowed, (list, tuple)):
            condition = (key in allowed)
        elif isinstance(allowed, str):
            condition = (key == allowed)
        if condition is True:
            break
    os.system("stty -raw echo")
    return key

def gen_students():
    dirs = os.listdir("{}/".format(main_folder))
    students_list = []
    students = {}
    for d in dirs:
        students_list.append(Student("{}/{}".format(main_path, d)))
    for s in students_list:
        students[s.username] = s
    return students

def grade(students):
    for s in students.values():
        s.test_scripts()
        s.save()
    clear()
    for s in students.values():
        print(s, "\n")

if __name__ == "__main__":
    students = gen_students()
    grade(students)
