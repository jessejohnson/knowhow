from rest_framework import routers
from apps.lectures.views import LearningContentViewSet, TopicViewSet
from apps.questions.views import EssayQuestionViewSet, MultipleChoiceQuestionViewSet, CaseStudyViewSet, CaseStudyQuestionViewSet

router = routers.DefaultRouter()
router.register(r'lectures', LearningContentViewSet)
router.register(r'topics', TopicViewSet)
router.register(r'essayqs', EssayQuestionViewSet)
router.register(r'mcqs', MultipleChoiceQuestionViewSet)
router.register(r'cases', CaseStudyViewSet)
router.register(r'casesqs',CaseStudyQuestionViewSet)