from marshmallow_sqlalchemy import ModelSchema
from marshmallow_sqlalchemy.fields import Nested
from task.models import Survey,Question
from marshmallow import Schema, fields, ValidationError

class QuestionsSchema(ModelSchema):
    class Meta:
        model = Question

class SurveysSchema(ModelSchema):
    questions = Nested(QuestionsSchema,many=True,exclude=("id","survey"))
    class Meta:
        model = Survey



surveys_schema = SurveysSchema(many=True)


# Custom validator
def must_not_be_blank(data):
    if not data:
        raise ValidationError("Data not provided.")



# ----------------------schemas------------------------------
class QuestionSchema(Schema):
    id = fields.Int(dump_only=True)
    body = fields.Str()
    note = fields.Str()
    
class SurveySchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str()
    description = fields.Str()
    questions = fields.List(fields.Nested(QuestionSchema(only=("body","note"))))
    start_date = fields.DateTime(dump_only=True)
    end_date = fields.DateTime(dump_only=True)
    

    
# survey schema
survey_schema = SurveySchema()

# questions schemas
question_schema = QuestionSchema()
questions_schema = QuestionSchema(many=True) 