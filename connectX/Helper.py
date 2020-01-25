{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 37,
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "def reformat(obs):\n",
    "    board = obs['board']\n",
    "    arr = np.array(board).reshape(6,7)\n",
    "    return arr\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "metadata": {},
   "outputs": [],
   "source": [
    "def reformatT(obs):\n",
    "    board = obs['board']\n",
    "    arr = np.array(board).reshape(6,7)\n",
    "    return np.transpose(arr)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "metadata": {},
   "outputs": [],
   "source": [
    "def flip(board):\n",
    "    return board[::-1]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "metadata": {},
   "outputs": [],
   "source": [
    "def create_zero():\n",
    "    return np.array([0]*42).reshape(6,7)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "metadata": {},
   "outputs": [],
   "source": [
    "\"\"\"TO CHECK\"\"\"\n",
    "def fall(board, col):\n",
    "    i = 5\n",
    "    while i >= 0:\n",
    "        if board[i][col] == 0:\n",
    "            return i\n",
    "        i = i - 1\n",
    "def fallext(board, col, turn):\n",
    "    i = fall(board, col)\n",
    "    board2 = board.copy()\n",
    "    board2[i][col] = turn\n",
    "    return board2\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "def valid_move(board):\n",
    "    l = list(board[0])\n",
    "    \n",
    "    return l.index(0)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "def check_valid_move(board, i):\n",
    "    if board[0][i] == 0:\n",
    "        return True\n",
    "    else:\n",
    "        return False"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "metadata": {},
   "outputs": [],
   "source": [
    "\"\"\"TO CHECK\"\"\"\n",
    "def create_diag(board):\n",
    "    h, w = board.shape\n",
    "    diag = []\n",
    "    for i in range(h + w + 1):\n",
    "        l = []\n",
    "        for j in range(h):\n",
    "            k = i - j\n",
    "            if k >= 0 and k <= w-1:\n",
    "                l.append([j,k])\n",
    "                #print([j,k])\n",
    "        diag.append(l)\n",
    "    return diag"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "metadata": {},
   "outputs": [],
   "source": [
    "def resolve_line(l, board):\n",
    "    return [board[ind[0]][ind[1]] for ind in l]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "metadata": {},
   "outputs": [],
   "source": [
    "def check_win_line_1(l):\n",
    "    count = 0\n",
    "    for i in range(len(l)):\n",
    "        if l[i] == 1:\n",
    "            count = count + 1\n",
    "        else:\n",
    "            count = 0\n",
    "        if count == 4:\n",
    "            return 1\n",
    "    return 0\n",
    "\n",
    "\n",
    "def check_win_line_2(l):\n",
    "    count = 0\n",
    "    for i in range(len(l)):\n",
    "        if l[i] == 2:\n",
    "            count = count + 1\n",
    "        else:\n",
    "            count = 0\n",
    "        if count == 4:\n",
    "            return 2\n",
    "    return 0\n",
    "def check_win_line(l):\n",
    "    if check_win_line_1(l) == 1:\n",
    "        return 1\n",
    "    elif check_win_line_2(l) == 2:\n",
    "        return 2\n",
    "    else:\n",
    "        return 0\n",
    "    return 0\n",
    "def check_win_h(board):\n",
    "    for x in range(len(board)):\n",
    "        if check_win_line(board[x]) != 0:\n",
    "            return check_win_line(board[x])\n",
    "    return 0\n",
    "def check_win_v(board):\n",
    "    boardt = np.transpose(board)\n",
    "    for x in range(len(boardt)):\n",
    "        if check_win_line(boardt[x]) != 0:\n",
    "            return check_win_line(boardt[x])\n",
    "    return 0\n",
    "def check_win_d_f(board):\n",
    "    for l in create_diag(board):\n",
    "        if check_win_line(resolve_line(l, board)) != 0:\n",
    "            return check_win_line(resolve_line(l, board))\n",
    "    return 0\n",
    "def check_win_d_b(board):\n",
    "    boardf = flip(board)\n",
    "    for l in create_diag(boardf):\n",
    "        if check_win_line(resolve_line(l, boardf)) != 0:\n",
    "            return check_win_line(resolve_line(l, boardf))\n",
    "    return 0\n",
    "def check_winner(board):\n",
    "    if check_win_h(board) != 0:\n",
    "        return check_win_h(board)\n",
    "    if check_win_v(board) != 0:\n",
    "        return check_win_v(board)\n",
    "    if check_win_d_f(board) != 0:\n",
    "        return check_win_d_f(board)\n",
    "    if check_win_d_b(board) != 0:\n",
    "        return check_win_d_b(board)\n",
    "    return 0"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "metadata": {},
   "outputs": [],
   "source": [
    "def check_win_line_1_alt(l, score, turn):\n",
    "    count = 0\n",
    "    for i in range(len(l)):\n",
    "        if l[i] == 1:\n",
    "            count = count + 1\n",
    "        else:\n",
    "            count = 0\n",
    "        if count == score:\n",
    "            return 1\n",
    "    return 0\n",
    "\n",
    "\n",
    "def check_win_line_2_alt(l, score, turn):\n",
    "    count = 0\n",
    "    for i in range(len(l)):\n",
    "        if l[i] == 2:\n",
    "            count = count + 1\n",
    "        else:\n",
    "            count = 0\n",
    "        if count == score:\n",
    "            return 2\n",
    "    return 0\n",
    "def check_win_line_alt(l, score, turn):\n",
    "    if turn == 1:\n",
    "        if check_win_line_1_alt(l,score, turn) == turn:\n",
    "            return turn\n",
    "    if turn == 2:\n",
    "        if check_win_line_2_alt(l,score, turn) == turn:\n",
    "            return turn\n",
    "    return 0\n",
    "def check_win_h_alt(board,score, turn):\n",
    "    for x in range(len(board)):\n",
    "        if check_win_line_alt(board[x],score, turn) != 0:\n",
    "            return check_win_line_alt(board[x],score, turn)\n",
    "    return 0\n",
    "def check_win_v_alt(board,score, turn):\n",
    "    boardt = np.transpose(board)\n",
    "    for x in range(len(boardt)):\n",
    "        if check_win_line_alt(boardt[x],score, turn) != 0:\n",
    "            return check_win_line_alt(boardt[x],score, turn)\n",
    "    return 0\n",
    "def check_win_d_f_alt(board,score, turn):\n",
    "    for l in create_diag(board):\n",
    "        if check_win_line_alt(resolve_line(l, board),score, turn) != 0:\n",
    "            return check_win_line_alt(resolve_line(l, board),score, turn)\n",
    "    return 0\n",
    "def check_win_d_b_alt(board,score, turn):\n",
    "    boardf = flip(board)\n",
    "    for l in create_diag(boardf):\n",
    "        if check_win_line_alt(resolve_line(l, boardf),score, turn) != 0:\n",
    "            return check_win_line_alt(resolve_line(l, boardf),score, turn)\n",
    "    return 0\n",
    "def check_winn(board, score, turn):\n",
    "    if check_win_h_alt(board, score, turn) != 0:\n",
    "        return check_win_h_alt(board, score, turn)\n",
    "    if check_win_v_alt(board, score, turn) != 0:\n",
    "        return check_win_v_alt(board, score, turn)\n",
    "    if check_win_d_f_alt(board, score, turn) != 0:\n",
    "        return check_win_d_f_alt(board, score, turn)\n",
    "    if check_win_d_b_alt(board, score, turn) != 0:\n",
    "        return check_win_d_b_alt(board, score, turn)\n",
    "    return 0\n",
    "\n",
    "def check_score(board,turn):\n",
    "    for i in [4,3,2,1]:\n",
    "        if check_winn(board, i, turn) != 0:\n",
    "            return i\n",
    "    return 0"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "def binary(val):\n",
    "    if val == 0:\n",
    "        return [0, 0]\n",
    "    elif val == 1:\n",
    "        return [1, 0]\n",
    "    elif val == 2:\n",
    "        return [0, 1]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "def switch(val):\n",
    "    return val[::-1]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "def reformat2(board_obj_obj):\n",
    "    board = board_obj_obj.board.copy()\n",
    "    #print(board)\n",
    "    board_reformat = np.zeros([6, 7, 2])\n",
    "    for i in range(len(board)):\n",
    "        for j in range(len(board[i])):\n",
    "            board_reformat[i][j][0] = binary(board[i][j])[0]\n",
    "            board_reformat[i][j][1] = binary(board[i][j])[1]\n",
    "    return board_reformat\n",
    "            \n",
    "            "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "def switch_reformat(board):\n",
    "    board2 = np.zeros_like(board)\n",
    "    for i in range(len(board)):\n",
    "        for j in range(len(board[i])):\n",
    "            board2[i][j] = switch(board[i][j])\n",
    "    return board2        \n",
    "            "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "def check_valid(board):\n",
    "        if 0 in board[0]:\n",
    "            return True\n",
    "        else:\n",
    "            return False"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "def evaluate(board):\n",
    "        if check_winner(board) == 1:\n",
    "            return 1\n",
    "        elif check_winner(board) == 2:\n",
    "            return 0\n",
    "        else: \n",
    "            if check_valid(board) == False:\n",
    "                return 0.5\n",
    "            else:\n",
    "                return 'Not finished Game'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "def unzip(myOrderedDict):\n",
    "    return list(list(myOrderedDict.items())[1])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "def prop_choice(l):\n",
    "    x = np.zeros_like(l)\n",
    "    x[0] = l[0]\n",
    "    for i in range(1, len(l)):\n",
    "        x[i] = x[i-1] + l[i]\n",
    "    v = np.random.uniform() * x[-1]\n",
    "    for i in range(len(l) - 1):\n",
    "        if v < l[i+1]:\n",
    "            return i\n",
    "    return len(l) - 2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "def turn_check(board):\n",
    "count1 = 0\n",
    "count2 = 0\n",
    "for i in range(6):\n",
    "    for j in range(7):\n",
    "        if board[i][j] == 1:\n",
    "            count1 += 1\n",
    "        if board[i][j] == 2:\n",
    "            count2 += 1\n",
    "if count1 > count2:\n",
    "    return 2\n",
    "else:\n",
    "    return 1
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
