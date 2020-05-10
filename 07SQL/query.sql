
--1 List employee number, last name, first name, sex, and salary of each employee 
SELECT employees.emp_no,last_name,first_name,sex,salary 
FROM employees
INNER JOIN salaries on employees.emp_no = salaries.emp_no
;

--2 List first name, last name, and hire date for employees hired in 1986
SELECT * FROM employees
WHERE hire_date BETWEEN '1986-01-01' AND '1986-01-31'
;

--3 List the manager of each department with: department number, department name, the manager's employee number, last name, first name
SELECT departments.dept_no, dept_name, employees.emp_no,employees.last_name, employees.first_name 
FROM departments
INNER JOIN dept_manager ON dept_manager.dept_no = departments.dept_no
	JOIN employees ON employees.emp_no = dept_manager.emp_no
;

--4 List the department of each employee with employee number, last name, first name, and department name
SELECT employees.emp_no, employees.last_name, employees.first_name, departments.dept_name
FROM ((employees
INNER JOIN dept_emp ON employees.emp_no = dept_emp.emp_no)
	JOIN departments ON dept_emp.dept_no = departments.dept_no)
;

--5 List first name, last name, and sex for employees whose first name is "Hercules" and last names begin with "B."
SELECT * FROM employees
WHERE first_name LIKE 'Hercules'
AND last_name LIKE 'B%'
;

--6 List all employees in the Sales department, including their employee number, last name, first name, and department name
SELECT employees.emp_no, employees.last_name, employees.first_name, departments.dept_name
FROM ((employees
	INNER JOIN dept_emp ON employees.emp_no = dept_emp.emp_no)
		JOIN departments ON dept_emp.dept_no = departments.dept_no)
WHERE departments.dept_name LIKE 'Sales'
;

--7 List all employees in the Sales and Development departments, including their employee number, last name, first name, and department name
SELECT employees.emp_no, employees.last_name, employees.first_name, departments.dept_name
FROM employees 
INNER JOIN dept_emp ON employees.emp_no = dept_emp.emp_no
	JOIN departments ON departments.dept_no = dept_emp.dept_no
WHERE departments.dept_name = 'Development'
OR departments.dept_name = 'Sales'
;

--8 List the frequency count of employee last names in descending order
SELECT last_name, COUNT(*) AS name_count
FROM employees
GROUP BY last_name
ORDER BY name_count DESC
;

