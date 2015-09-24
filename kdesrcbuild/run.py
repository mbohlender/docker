#!/usr/bin/env python2
import sh
from sh import docker
import subprocess
import settings
import dockerutils
import argparse

def srcbuild(options):
    main(options.command, options.env, options.args)

def setupSubparser(parser):
    parser.add_argument("env", help = "environment to use")
    parser.add_argument("command", help = "command to use (should be another subparser). Is used for the project in case of arbitray command.")
    parser.add_argument('args', nargs=argparse.REMAINDER)
    parser.set_defaults(func=srcbuild)

def main(command, environment, commandargs):
    runargs = ( "-ti",
        "--rm",
        "--privileged",
        "-v", "~/kdebuild/{}:/work".format(environment),
        "-v", "{}/{}/{}/kdesrc-buildrc:/home/developer/.kdesrc-buildrc".format(settings.SCRIPT_DIR, "kdesrcbuild", environment),
        "-v", "{}/{}/bashrc:/home/developer/.bashrc".format(settings.SCRIPT_DIR, "kdesrcbuild"),
        "-v", "{}/{}/build-de.sh:/home/developer/build-de.sh".format(settings.SCRIPT_DIR, "kdesrcbuild"),
    )
    image="fedora-kdedev"
    translatePathsToHost = "sed 's/\/work\//~\/kdebuild\/{environment}\//g'".format(environment=environment)

    if command == "shell":
        subprocess.call("docker run {defaultargs} {image} -c bash".format(defaultargs=" ".join(runargs), image=image), shell=True, cwd=settings.SCRIPT_DIR+"/kdesrcbuild")
    elif command == "kdesrcbuild":
        args = ()
        #Create the root dir so it is created with the correct rights
        subprocess.call("mkdir -p ~/kdebuild/{}".format(environment), shell=True)
        command = '/home/developer/kdesrc-build/kdesrc-build'
        if commandargs:
            command += ' ' + ' '.join(commandargs);
        subprocess.call("docker run {defaultargs} {args} {image} -c 'source /home/developer/.bashrc && {command}' | {translatePathsToHost}".format(defaultargs=" ".join(runargs), args=" ".join(args), image=image, command=command, translatePathsToHost=translatePathsToHost), shell=True, cwd=settings.SCRIPT_DIR+"/kdesrcbuild")
    else:
        project = command
        print("Installing {}".format(project))
        args = ("-w", "/work/build/{project}".format(project=project))
        command = " ".join(commandargs)
        subprocess.call("docker run {defaultargs} {args} {image} -c 'source /home/developer/.bashrc && {command}' | {translatePathsToHost}".format(defaultargs=" ".join(runargs), args=" ".join(args), image=image, command=command, translatePathsToHost=translatePathsToHost), shell=True, cwd=settings.SCRIPT_DIR+"/kdesrcbuild")
