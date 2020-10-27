# -*- coding: utf-8 -*-
import unittest
from engine.api import *


class TestEngine(unittest.TestCase):
    def test_exclude_noises(self):
        text = '!@#$%^^&*()，。/-_=+;:こんにちは'
        self.assertEqual('こんにちは', judge_engine.exclude_noise(text))

    def test_judge_dajare(self):
        texts = [
            [True, '布団が吹っ飛んだ'],
            [True, '芸無なゲーム'],
            [True, 'ダジャレを言うのは誰じゃ'],
            [True, '紅茶が凍っちゃった'],
            [True, 'ニューヨークで入浴'],
            [True, 'アヒージョはアチーよ'],
            [True, '過大な課題www'],
            [True, '臭いサイ'],
            [True, 'この卵エッグ'],
            [True, 'かきくカケク'],
            [True, 'かきあカキァ'],
            [True, 'かきくサキク'],
            [True, 'かきくケキク'],
            [True, 'かきくけカキエク-ん'],
            [True, 'かきくけカキケク-ん'],
            [True, 'かきくカキック-んン'],
            [True, 'かきくカキンク-んン'],
            [True, 'かきくカキーク-んン'],
            [True, 'かきいカキー-んン'],
            [True, 'かこうカコー-んン'],
            [True, 'かけいカケー-んン'],
            [True, 'あいうアユー'],
            [True, 'しゃんあサンア'],
            [False, 'あいうあいう-ん'],
            [False, 'あいあいあいあいあいあい-かきくけこ'],
            [False, '布団が吹っ飛んだ布団が吹っ飛んだあいうえおかきくけこさしすせ'],
            [False, 'See you later, alligator'],
            [False, '野球は野球だ'],
            [False, 'AはAだ'],
            [False, 'ああいあい'],
            [False, 'テストあいうテストかきく'],
            [False, 'あいうえあいうえ-あ'],
            [False, 'あいうえおあいうえお-あ'],
        ]
        for text in texts:
            self.assertEqual(
                text[0],
                judge_engine.is_dajare(text[1], False)
            )

    def test_eval(self):
        score = eval_engine.eval("布団が吹っ飛んだ")
        self.assertTrue(score >= 1.0 and score <= 5.0)

    @unittest.skipIf(not katakanizer.token_valid, 'TESTSKIP')
    def test_katakanize(self):
        texts = [
            ['コンニチハ', 'こんにちは'],
            ['チョオマエ', 'ちょwお前www'],
            ['エービーシーディー', 'ABCD'],
            ['エービーシー', 'ABC'],
            ['', 'abcd'],
            ['ハロー', 'hello'],
        ]
        for text in texts:
            self.assertEqual(
                text[0],
                katakanizer.katakanize(text[1])
            )

    @unittest.skipIf(not sensitive_checker.token_valid, 'TESTSKIP')
    def test_sensitive_tags(self):
        text = '殺人，麻薬'
        self.assertEqual(
            ['傷害', '恐喝', '殺人', '脅迫', '薬物', '覚せい剤', '麻薬'],
            sensitive_checker.check(text))