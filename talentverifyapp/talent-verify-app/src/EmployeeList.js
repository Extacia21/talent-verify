import React, { useEffect, useState } from 'react';
import axios from 'axios';
import config from '../config';

function EmployeeList() {
  const [employees, setEmployees] = useState([]);

  useEffect(() => {
    async function fetchEmployees() {
  try {
    const response = await axios.get('https://pycharm/navigate/reference?project=talentverifyapp&path=talentverifyapp.com/api/employees/');
    setEmployees(response.data);
  } catch (error) {
    console.error(error);
  }
}

    fetchEmployees();
  }, []);

  return (
    <div>
      <h1>Employees</h1>
      <table>
        <thead>
          <tr>
            <th>Name</th>
            <th>ID Number</th>
            <th>Company</th>
            <th>Department</th>
            <th>Role</th>
            <th>Date Started</th>
            <th>Date Left</th>
            <th>Duties</th>
          </tr>
        </thead>
        <tbody>
          {employees.map(({ id, name, employee_id, company, department, role, date_started, date_left, duties }, idx) => (
            <tr key={idx}>
              <td>{name}</td>
              <td>{employee_id}</td>
              <td>{company.name}</td>
              <td>{department}</td>
              <td>{role}</td>
              <td>{date_started}</td>
              <td>{date_left || '-'}</td>
              <td>{duties}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default EmployeeList;