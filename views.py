from django.shortcuts import render, get_object_or_404
from .models import Course, Submission, Choice, Learner, Question

def submit(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    learner = Learner.objects.first()

    selected = request.POST.getlist('choices')
    selected_ids = [int(x) for x in selected]

    submission = Submission.objects.create(learner=learner)
    submission.choices.set(selected_ids)

    return show_exam_result(request, course.id, submission.id)


def show_exam_result(request, course_id, submission_id):
    course = get_object_or_404(Course, pk=course_id)
    submission = get_object_or_404(Submission, pk=submission_id)

    selected_ids = [choice.id for choice in submission.choices.all()]

    total_score = 0
    possible_score = 0

    for question in Question.objects.filter(lesson__course=course):
        possible_score += 1
        if question.is_get_score(selected_ids):
            total_score += 1

    return render(request, 'result.html', {
        'course': course,
        'selected_ids': selected_ids,
        'grade': total_score,
        'possible': possible_score
    })