#!/usr/bin/python2.7
"""
Program to build graphics and test parallel programs

It builds dependancies of
* execution time to processes number
* acceleration to processes number

Author: Evgeny Yulyugin
Year: 2014
"""

import sys
import argparse
import os
import subprocess

gnuplot_file = "builder.graph"

def compile(compiler, source):
    """
    Compile given file with given compiler and extra options.
    Base option: -Werror -O2
    """
    compile_options = ["-Werror", "-O2"]
    command = list()
    command.append(compiler)
    command.extend(compile_options)
    command.append(source)
    return subprocess.call(command)

def mkenv():
    parser = argparse.ArgumentParser(add_help=True, version = '0.1',
                                     description="Graphics builder.")
    parser.add_argument("--compiler", type=str, action="store", default="mpicc",
                        help="Path to mpicc compiler.")
    parser.add_argument("--mpirun", type=str, action="store", default="mpirun",
                        help="Path to mpi starter.")
    parser.add_argument("--gnuplot", type=str, action="store", default="gnuplot",
                        help="Path to gnuplot executable file.")
    parser.add_argument("source", type=str, action="store",
                        help="Path to the source file.")
    parser.add_argument("--options", type=str, action="store",
                        help="Command line arguments for tested program.")
    args = parser.parse_args()
    return args

def clean():
    os.unlink("a.out")

def main():
    env = mkenv()
    if compile(env.compiler, env.source) != 0:
        return 1

    clean()
    return 0

if __name__ == "__main__":
    sys.exit(main())
