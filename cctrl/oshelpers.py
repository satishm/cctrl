# -*- coding: utf-8 -*-

"""
    Copyright 2010 cloudControl UG (haftungsbeschraenkt)

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""
import os
from cctrl.error import InputErrorException


def isValidFile(filename):
        """
            Is the given filename a valid file?
        """
        return os.path.isfile(os.path.abspath(filename))


def readContentOf(filename):
    """
        Read a given file's content into a string
        Returns contents of given file as string, otherwise "None"
    """
    file_content = ''

    # check if file exists
    if not os.path.isfile(os.path.abspath(filename)):
        raise InputErrorException('FileNotFound')

    # open file and read into string
    try:
        open_file = open(os.path.abspath(filename), 'r')
        file_content = str(open_file.read())
    except IOError:
        raise InputErrorException('FileReadOrWriteFailed')

    # pass back content
    return file_content


def repository_type(repo_path):
    """
        Find out which repository type the given directory/repo has.
        We can only identify (and use) GIT and BAZAAR.
    """
    repository_type = ""

    # Check the current directory for .git or .bzr
    absolute_repo_path = os.path.abspath(repo_path)

    if os.path.exists(absolute_repo_path + "/.git"):
        repository_type = 'git'
    elif os.path.exists(absolute_repo_path + "/.bzr"):
        repository_type = 'bzr'

    return repository_type


def which(programs):
    """
        from http://stackoverflow.com/questions/377017/ \
        test-if-executable-exists-in-python/377028#377028
    """
    def is_exe(file_path):
        return os.path.exists(file_path) and os.access(file_path, os.X_OK)

    for program in programs:
        file_path, file_name = os.path.split(program)  # @UnusedVariable
        if file_path:
            if is_exe(program):
                return program
        else:
            for path in os.environ["PATH"].split(os.pathsep):
                exe_file = os.path.join(path, program)
                if is_exe(exe_file):
                    return exe_file

    return None


def check_installed_rcs(name):
    """
        Check if either "bzr" or "git" is installed (and can be found
        via PATH variable)
    """
    rcs_executables = {
        'bzr': ['bzr.exe', 'bzr.bat', 'bzr'],
        'git': ['git', 'git.exe', 'git.cmd']}
    return which(rcs_executables[name])
