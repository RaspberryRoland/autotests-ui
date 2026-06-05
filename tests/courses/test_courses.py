import pytest

from fixtures.pages import courses_list_page
from pages.authentication.login_page import LoginPage
from pages.courses.courses_list_page import CoursesListPage
from pages.courses.create_course_page import CreateCoursePage


@pytest.mark.courses
@pytest.mark.regression
class TestCourses:
    def test_create_course(self, courses_list_page: CoursesListPage,
                           create_course_page: CreateCoursePage):
        courses_list_page.visit(
            'https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create')

        create_course_page.create_course_toolbar_view_component.check_visible()
        create_course_page.image_upload_widget.check_visible(
            is_image_uploaded=False)
        create_course_page.create_course_form_component.check_visible("", "",
                                                                      "", "0",
                                                                      "0")

        create_course_page.create_course_exercises_toolbar_view_component.check_visible()
        create_course_page.check_visible_exercises_empty_view()

        create_course_page.image_upload_widget.upload_preview_image(
            './testdata/files/image.png')
        create_course_page.image_upload_widget.check_visible(
            is_image_uploaded=True)
        create_course_page.create_course_form_component.fill("Playwright",
                                                             "2 weeks",
                                                             "Playwright",
                                                             "100", "10")
        create_course_page.create_course_toolbar_view_component.click_create_course_button()

        courses_list_page.toolbar_view.check_visible()
        courses_list_page.course_view.check_visible(0, "Playwright", "100",
                                                    "10",
                                                    "2 weeks")

    def test_empty_courses_list(self, courses_list_page: CoursesListPage):
        courses_list_page.visit(
            "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")
        courses_list_page.navbar.check_visible('username')
        courses_list_page.sidebar.check_visible()

        courses_list_page.toolbar_view.check_visible()
        courses_list_page.check_visible_empty_view()

    def test_edit_course(
            self,
            courses_list_page: CoursesListPage,
            create_course_page: CreateCoursePage):

        courses_list_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create')
        create_course_page.create_course_form_component.fill(title='Test Title', estimated_time="30", description="Test Descr",
             max_score="10", min_score="50")
        create_course_page.image_upload_widget.upload_preview_image('./testdata/files/image.png')
        create_course_page.create_course_toolbar_view_component.click_create_course_button()
        courses_list_page.course_view.check_visible(index=0, title='Test Title', estimated_time="30",
             max_score="10", min_score="50")

        courses_list_page.course_view.menu.click_edit(index=0)

        create_course_page.create_course_form_component.fill(
            title='New Test Title', estimated_time="20", description="New Test Descr",
            max_score="20", min_score="10")
        create_course_page.create_course_toolbar_view_component.click_create_course_button()
        courses_list_page.course_view.check_visible(index=0, title='New Test Title',
                                                    estimated_time="20",
                                                    max_score="20",
                                                    min_score="10")
