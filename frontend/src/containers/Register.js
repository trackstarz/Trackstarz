import React, { useState } from 'react';
import * as actions from '../store/actions/auth';
import { connect } from 'react-redux';
import {
  Form,
  Input,
  Button
} from 'antd';
import { NavLink } from 'react-router-dom';
import '../style.css';

const RegistrationForm = (props) => {
  const [form] = Form.useForm();
  const [confirmDirty, setConfirmDirty] = useState(false);

  const handleSubmit = (values) => {
    props.onAuth(
      values.username,
      values.email,
      values.password,
      values.confirm
    );
    props.history.push('/');
  };

  const handleConfirmBlur = (event) => {
    const { value } = event.target;
    setConfirmDirty(confirmDirty || !!value);
  };

  const compareToFirstPassword = (rule, value, callback) => {
    if (value && value !== form.getFieldValue('password')) {
      callback('Two passwords that you enter is inconsistent!');
    } else {
      callback();
    }
  };

  const validateToNextPassword = (rule, value, callback) => {
    if (value && confirmDirty) {
      form.validateFields(['confirm'], { force: true });
    }
    callback();
  };

  return (
    <Form form={form} onFinish={handleSubmit}>
      <Form.Item
        name="username"
        rules={[{ required: true, message: 'Please input your username!' }]}
      >
        <Input placeholder="Username" />
      </Form.Item>

      <Form.Item
        name="email"
        rules={[
          {
            type: 'email',
            message: 'The input is not valid E-mail!',
          },
          {
            required: true,
            message: 'Please input your E-mail!',
          },
        ]}
      >
        <Input placeholder="Email" />
      </Form.Item>

      <Form.Item
        name="password"
        rules={[
          {
            required: true,
            message: 'Please input your password!',
          },
          {
            validator: validateToNextPassword,
          },
        ]}
      >
        <Input.Password type="password" placeholder="Password" />
      </Form.Item>

      <Form.Item
        name="confirm"
        dependencies={['password']}
        rules={[
          {
            required: true,
            message: 'Please confirm your password!',
          },
          {
            validator: compareToFirstPassword,
          },
        ]}
      >
        <Input.Password
          type="password"
          placeholder="Confirm Password"
          onBlur={handleConfirmBlur}
        />
      </Form.Item>

      <Form.Item>
        <Button type="primary" htmlType="submit" style={{ marginRight: '10px' }}>
          Join
        </Button>
        Or
        <NavLink style={{ marginRight: '10px' }} to="/login/">
          Login
        </NavLink>
      </Form.Item>
    </Form>
  );
};

const mapStateToProps = (state) => {
  return {
    loading: state.loading,
    error: state.error,
  };
};

const mapDispatchToProps = (dispatch) => {
  return {
    onAuth: (username, email, password1, password2) =>
      dispatch(actions.authRegister(username, email, password1, password2)),
  };
};

export default connect(mapStateToProps, mapDispatchToProps)(RegistrationForm);
