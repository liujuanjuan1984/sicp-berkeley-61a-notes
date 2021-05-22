#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
practice by python for lessone 02

需求：汉诺塔操作路径

把高度为n的汉诺塔从起始位置挪到终点位置，计算出操作步骤

"""
n = 3  # 高度
pillars = range(3)  # 柱子编号，0是起点，2是终点
disks = range(n)  # 盘子编号，从小到大，0最小


def move_tower(n):
    move_tower(n - 1)
    move_tower()


# 如何抽象化？
