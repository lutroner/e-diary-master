from datacenter.models import Schoolkid, Chastisement, Lesson, Commendation, Mark
from random import choice
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned

COMMENDATIONS = ('Молодец!', 'Отлично!', 'Хорошо!', 'Гораздо лучше, чем я ожидал!', 'Ты меня приятно удивил!',
                 'Великолепно!', 'Прекрасно!', 'Ты меня очень обрадовал!', 'Именно этого я давно ждал от тебя!',
                 'Сказано здорово – просто и ясно!', 'Ты, как всегда, точен!', 'Очень хороший ответ!',
                 'Талантливо!', 'Ты сегодня прыгнул выше головы!', 'Я поражен!', 'Уже существенно лучше!')


def get_schoolkid_from_name(name):
    try:
        schoolkid = Schoolkid.objects.get(full_name=name)
        return schoolkid
    except ObjectDoesNotExist:
        raise ObjectDoesNotExist(f'Проверь правильность написания имени. Имя "{name}" не существует. \n'
                                 f'Имя нужно указывать полностью (ФИО) с заглавных букв.')


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
    while True:
        try:
            random_schoolkid_lesson = schoolkid_class_lessons.filter(subject__title=subject).order_by('?').first()
        except IndexError:
            raise IndexError(f'Проверь правильность написания названия предмета.'
                             f'Предмет "{subject}" не существует.')
        if not Commendation.objects.filter(created=random_schoolkid_lesson.date, schoolkid_id=schoolkid.id,
                                           subject_id=random_schoolkid_lesson.subject_id):
            Commendation.objects.create(created=random_schoolkid_lesson.date, schoolkid_id=schoolkid.id,
                                        subject_id=random_schoolkid_lesson.subject_id,
                                        teacher_id=random_schoolkid_lesson.teacher_id, text=choice(COMMENDATIONS))
            break
