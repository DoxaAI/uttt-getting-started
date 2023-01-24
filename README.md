# Getting Started with Ultimate Tic-tac-toe on DOXA

Here is everything you need to get started with the ultimate tic-tac-toe competition on DOXA! There is also more information available on the [DOXA UTTT competition page](https://doxaai.com/competition/uttt).

Feel free to fork this repository and use it as the base for implementing your own agents! You can also join the conversation on the [DOXA Discord server](https://discord.gg/MUvbQ3UYcf).

## Prerequisites

Before you begin, please ensure that you have Python 3.9+, NumPy and the DOXA CLI installed.

If you do not yet have the DOXA CLI installed, you may do so with `pip`:

```bash
pip install doxa-cli
```

## Implementing an agent

First, clone this repository if you have not already done so. Then, you can start implementing your first agent by modifying the `make_move()` method of the agent in `main.py`.

By default, the agent just plays moves at random. What interesting strategies can you come up with? 👀

## Submitting to DOXA

Before you can submit your agent to DOXA, you must first ensure that you are logged into the DOXA CLI. You can do so with the following command:

```bash
doxa login
```

Then, when you are ready to submit your agent (contained within the `agent` folder) to DOXA, run the following command:

```bash
doxa upload agent
```

Please ensure that the `agent` folder only contains the files you wish to upload to DOXA. If you have renamed your agent folder to something else, substitute `agent` for the new folder name.
