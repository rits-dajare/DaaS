from flask import Blueprint
from flask_restful import Api
from .api import API

from core import engine


class JudgeAPI(API):
    def _args_validation(self, args):
        return 'dajare' in args

    def _processing(self, args):
        result = {
            'is_dajare': None,
            'applied_rule': None,
        }

        result['is_dajare'] = engine.judge_engine.exec(args['dajare'])
        result['applied_rule'] = engine.judge_engine.applied_rule

        return result


bp = Blueprint('judge', __name__)
api = Api(bp)
api.add_resource(JudgeAPI, '')
