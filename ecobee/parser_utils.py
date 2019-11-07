"""
This module is responsible to have all the functions
related to parsing the job

"""
import argparse


def batch_job_args(parser):
    """
    add args related to batch job
    :param parser:
    :return:
    """
    parser.add_argument(
        "--input", dest="input", default="input.txt", help="Input file to process.",
    )
    parser.add_argument(
        "--output",
        dest="output",
        default="output.txt",
        help="Output file to write results to.",
    )
    return parser


def top_n_job_args(parser):
    """
    add args related to top_n jobs
    :param parser:
    :return:
    """
    parser.add_argument(
        "--top-n", default=10, type=int, help="Number of top entries to report."
    )
    parser.add_argument(
        "--time-period-secs",
        default=0,
        type=int,
        help="If two events are apart by this value of time, "
        "they are considered in separate sequences.",
    )
    return parser


def parse_top_n_job_args(argv):
    """
    Parse the given command line arguments.
    :param argv:
    :return: known and unknown args
    """
    parser = argparse.ArgumentParser()
    parser = batch_job_args(parser)
    parser = top_n_job_args(parser)
    return parser.parse_known_args(argv)
