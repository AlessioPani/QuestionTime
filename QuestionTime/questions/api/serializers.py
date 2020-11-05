from rest_framework import serializers
from questions.models import Answer, Question
import locale


# locale.setlocale(locale.LC_ALL, "it_IT.utf8")


class AnswerSerializer(serializers.ModelSerializer):
    '''
    Serializer for the Answer model.
    '''
    author = serializers.StringRelatedField(read_only=True)
    created_at = serializers.SerializerMethodField(read_only=True)
    likes_count = serializers.SerializerMethodField(read_only=True)
    user_has_voted = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Answer
        exclude = ["question", "voters", "updated_at"]

    def get_created_at(self, instance):
        '''
        Function that provides the value of the serializer MethodField
        "created_at" attribute.
        '''
        return instance.created_at.strftime('%d %B %Y')

    def get_likes_count(self, instance):
        '''
        Function that provides the value of the serializer MethodField
        "likes_count" attribute.
        '''
        return instance.voters.count()

    def get_user_has_voted(self, instance):
        '''
        Function that provides the value of the serializer MethodField
        "user_has_voted" attribute.
        '''
        request = self.context.get("request")
        return instance.voters.filter(pk=request.user.pk).exists()


class QuestionSerializer(serializers.ModelSerializer):
    '''
    Serializer for the Question model.
    '''
    author = serializers.StringRelatedField(read_only=True)
    created_at = serializers.SerializerMethodField(read_only=True)
    slug = serializers.SlugField(read_only=True)
    answers_count = serializers.SerializerMethodField(read_only=True)
    user_has_answered = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Question
        exclude = ["updated_at"]

    def get_answers_count(self, instance):
        '''
        Function that provides the value of the serializer MethodField
        "answers_count" attribute.
        '''
        return instance.answers.count()

    def get_created_at(self, instance):
        '''
        Function that provides the value of the serializer MethodField
        "created_at" attribute.
        '''
        return instance.created_at.strftime('%d %B %Y')

    def get_user_has_answered(self, instance):
        '''
        Function that provides the value of the serializer MethodField
        "user_has_answered" attribute.
        '''
        request = self.context.get("request")
        return instance.answers.filter(author=request.user).exists()
