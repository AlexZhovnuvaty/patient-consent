# Copyright 2017 Intel Corporation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# -----------------------------------------------------------------------------

import sys
import argparse

from sawtooth_sdk.processor.core import TransactionProcessor
from sawtooth_sdk.processor.log import init_console_logging
from sawtooth_sdk.processor.log import log_configuration
from sawtooth_sdk.processor.config import get_log_config
# from sawtooth_sdk.processor.config import get_log_dir

from consent_processor.consent_common.helper import TP_PREFFIX_HEX6
from consent_processor.handler import ConsentTransactionHandler


def parse_args(args):
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawTextHelpFormatter)

    parser.add_argument(
        '-C', '--connect',
        default='tcp://localhost:4004',
        help='Endpoint for the validator connection')

    parser.add_argument('-v', '--verbose',
                        action='count',
                        default=0,
                        help='Increase output sent to stderr')

    return parser.parse_args(args)


def main(args=None):
    if args is None:
        args = sys.argv[1:]
    opts = parse_args(args)
    processor = None
    try:
        processor = TransactionProcessor(url=opts.connect)
        log_config = get_log_config(filename="consent_log_config.toml")

        # If no toml, try loading yaml
        if log_config is None:
            log_config = get_log_config(filename="consent_log_config.yaml")

        if log_config is not None:
            log_configuration(log_config=log_config)
        # else:
        #     log_dir = get_log_dir()
            # use the transaction consent_processor zmq identity for filename
            # log_configuration(
            # log_dir=log_dir,
            # name="healthcare-" + str(consent_processor.zmq_id)[2:-1])

        init_console_logging(verbose_level=opts.verbose)

        handler = ConsentTransactionHandler(TP_PREFFIX_HEX6)

        processor.add_handler(handler)

        processor.start()
    except KeyboardInterrupt:
        pass
    except Exception as e:  # pylint: disable=broad-except, invalid-name
        print("Error: {}".format(e), file=sys.stderr)
    finally:
        if processor is not None:
            processor.stop()


if __name__ == "__main__":
    main()
