#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, jsonify, abort, make_response, request
from engine.judge_engine import JudgeEngine
from engine.eval_engine import EvalEngine

app = Flask(__name__)

# dajare engine
judge_engine = JudgeEngine()
eval_engine = EvalEngine()


@app.route('/dajare/judge', methods=['GET'])
def dajare_judge():
    '''
    uri：
        /dajare/judge
    method：
        GET
    headers：
        'Content-Type':'application/json'
    query：
        dajare: String,
    response：
        {
            is_dajare: Boolean,
            include_sensitive: Boolean,
            sensitive_tags: [String]
            status: String,
        }
    '''

    # received query params
    params = dict(request.args)

    response = {
        'is_dajare': False,
        'include_sensitive': False,
        'sensitive_tags': [],
        'status': 'OK',
    }

    # whether params could be received
    if 'dajare' not in params:
        response['status'] = 'NG'
        return make_response(jsonify(response), 400)

    # judge
    if judge_engine.is_dajare(params['dajare']):
        response['is_dajare'] = True

    # sensitive check
    response['sensitive_tags'] = \
        judge_engine.find_sensitive_tags(params['dajare'])
    if response['sensitive_tags'] != []:
        response['include_sensitive'] = True

    return make_response(jsonify(response), 200)


@app.route('/dajare/evaluate', methods=['GET'])
def dajare_evaluate():
    '''
    uri：
        /dajare/evaluate
    method：
        GET
    headers：
        'Content-Type':'application/json'
    query：
        dajare: String,
    response：
        {
            score: Number,
            status: String,
        }
    '''

    # received query params
    params = dict(request.args)

    response = {
        'score': 0,
        'status': 'OK',
    }

    # whether params could be received
    if 'dajare' not in params:
        response['status'] = 'NG'
        return make_response(jsonify(response), 400)

    # eval
    response['socre'] = eval_engine.eval(params['dajare'])

    return make_response(jsonify(response), 200)


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)