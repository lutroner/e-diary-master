from datacenter.models import *
from random import choice

vanya = Schoolkid.objects.get(full_name='Фролов Иван Григорьевич')
feo = Schoolkid.objects.filter(full_name__contains='Голубев Феофан')

COMMENDATIONS = ('Молодец!', 'Отлично!', 'Хорошо!', 'Гораздо лучше, чем я ожидал!', 'Ты меня приятно удивил!',
                 'Великолепно!', 'Прекрасно!', 'Ты меня очень обрадовал!', 'Именно этого я давно ждал от тебя!',
                 'Сказано здорово – просто и ясно!', 'Ты, как всегда, точен!', 'Очень хороший ответ!',
                 'Талантливо!', 'Ты сегодня прыгнул выше головы!', 'Я поражен!', 'Уже существенно лучше!')


def get_schoolkid_from_name(name):
    schoolkid_query = Schoolkid.objects.filter(full_name__contains=name)
    if len(schoolkid_query) > 1:
        raise TypeError(f'Учеников "{name}" больше одного. Уточните имя ученика!')
    if not schoolkid_query:
        raise TypeError( f'Имя "{name}" не найдено.')
    schoolkid = schoolkid_query[0]
    return schoolkid


def fix_marks(name):
    schoolkid = get_schoolkid_from_name(name)
    schoolkid_marks = Mark.objects.filter(schoolkid=schoolkid)
    for mark in schoolkid_marks:
        if mark.points in (2, 3):
            mark.points = 5
            mark.save()


def remove_chastisements(name):
    schoolkid = get_schoolkid_from_name(name)
    schoolkid_chastisements = Chastisement.objects.filter(schoolkid=schoolkid)
    schoolkid_chastisements.delete()


def create_commendation(name, subject):
    schoolkid = get_schoolkid_from_name(name)
    schoolkid_class_lessons = Lesson.objects.filter(year_of_study=schoolkid.year_of_study,
                                                    group_letter=schoolkid.group_letter)
    count = 0
    while True:
        schoolkid_subject = schoolkid_class_lessons.filter(subject__title=subject).order_by('-date')[count]
        if not Commendation.objects.filter(created=schoolkid_subject.date, schoolkid_id=schoolkid.id,
                                           subject_id=schoolkid_subject.subject_id):
            Commendation.objects.create(created=schoolkid_subject.date, schoolkid_id=schoolkid.id,
                                        subject_id=schoolkid_subject.subject_id,
                                        teacher_id=schoolkid_subject.teacher_id, text=choice(COMMENDATIONS))
            break
        count += 1

create_commendation('ваня', 'Русский язык')
