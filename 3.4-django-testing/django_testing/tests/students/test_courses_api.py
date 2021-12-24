import pytest
from django.urls import reverse
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT, HTTP_404_NOT_FOUND, \
    HTTP_400_BAD_REQUEST


# проверка получения первого курса
@pytest.mark.django_db
def test_get_first_course(api_client, course_factory):
    course_name = course_factory()

    url_get_details = reverse('courses-detail', args=(course_name.id,))
    response = api_client.get(url_get_details)

    assert response.status_code == HTTP_200_OK
    response_json = response.json()
    assert len(response_json) == 3
    assert response_json['name'] == str(course_name.name)


# проверка получения списка курсов
@pytest.mark.django_db
def test_get_courses_list(api_client, course_factory):
    course_name_first = course_factory()
    course_name_second = course_factory()

    url_get_first = reverse('courses-list')
    response = api_client.get(url_get_first)

    assert response.status_code == HTTP_200_OK
    response_json = response.json()
    assert len(response_json) == 2
    assert response_json[0]['name'] == course_name_first.name
    assert response_json[1]['name'] == course_name_second.name


# проверка получения курса по id
@pytest.mark.django_db
def test_get_course_by_name(api_client, course_factory):
    course_name = course_factory()

    url = reverse('courses-list')
    response = api_client.get(url, {'id': course_name.id})

    assert response.status_code == HTTP_200_OK
    response_json = response.json()
    assert len(response_json) == 1
    for obj in response_json:
        assert obj.get('id') == course_name.id


# проверка получения курса по name
@pytest.mark.django_db
def test_get_course_by_id(api_client, course_factory):
    course_name = course_factory()

    url = reverse('courses-list')
    response = api_client.get(url, {'name': course_name.name})

    assert response.status_code == HTTP_200_OK
    response_json = response.json()
    assert len(response_json) == 1
    for obj in response_json:
        assert obj.get('name') == str(course_name.name)


# проверка создания курса
@pytest.mark.django_db
def test_create_course(api_client, course_payload):
    url = reverse('courses-list')
    response = api_client.post(url, course_payload)

    assert response.status_code == HTTP_201_CREATED


# тест успешного обновления курса
@pytest.mark.django_db
def test_update_course(api_client, course_payload, course_factory):
    course_name = course_factory()
    url = reverse('courses-list') + str(course_name.id) + '/'
    response = api_client.patch(url, course_payload)

    assert response.status_code == HTTP_200_OK

    # дополнительно проверяем, что данные действительно обновились
    url_get = reverse('courses-list') + '?id=' + str(course_name.id)
    response = api_client.get(url_get)

    assert response.status_code == HTTP_200_OK
    response_json = response.json()
    assert len(response_json) == 1
    for obj in response_json:
        assert obj.get('name') == str(course_payload['name'])


# тест успешного удаления курса
@pytest.mark.django_db
def test_delete_course(api_client, course_factory):
    course_name = course_factory()
    url = reverse('courses-list') + str(course_name.id) + '/'
    response = api_client.delete(url)

    assert response.status_code == HTTP_204_NO_CONTENT

    # дополнительно проверяем, что данные действительно удалены
    response = api_client.get(url)
    assert response.status_code == HTTP_404_NOT_FOUND


@pytest.mark.parametrize(
    ['students_max_value', 'resp_moq'],
    (
        (0, HTTP_400_BAD_REQUEST),
        (1, HTTP_201_CREATED)
    )
)
@pytest.mark.django_db
def test_create_course_with_too_much_students(settings, api_client, course_factory, student_factory,
                                              students_max_value, resp_moq):

    settings.MAX_STUDENTS_PER_COURSE = students_max_value
    url = reverse('courses-list')

    payload = {
        "name": course_factory().name,
        'students': [student_factory().id]
    }

    response = api_client.post(url, payload)
    assert response.status_code == resp_moq
