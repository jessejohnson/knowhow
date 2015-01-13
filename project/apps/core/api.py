from rest_framework import routers
from .views import UserViewSet, TopicViewSet, ExamViewSet, PaperViewSet
from apps.lectures.views import LearningResourceViewSet
from apps.questions.views import EssayQuestionViewSet, MultipleChoiceQuestionViewSet, CaseStudyViewSet, CaseStudyQuestionViewSet
from apps.studentrecords.views import StudentRecordViewSet
from apps.tests.views import TestViewSet, TestTableViewSet

router = routers.DefaultRouter()
# router.register(r'signup', UserSignUpViewSet)
router.register(r'users', UserViewSet)
router.register(r'resources', LearningResourceViewSet)
router.register(r'topics', TopicViewSet)
router.register(r'exams', ExamViewSet)
router.register(r'papers', PaperViewSet)
router.register(r'essayqs', EssayQuestionViewSet)
router.register(r'mcqs', MultipleChoiceQuestionViewSet)
router.register(r'cases', CaseStudyViewSet)
router.register(r'casesqs',CaseStudyQuestionViewSet)
router.register(r'studentrecords',StudentRecordViewSet)
router.register(r'tests',TestViewSet)
router.register(r'testtables',TestTableViewSet)