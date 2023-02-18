import React from 'react';
import { Form, Input, Button } from 'antd';
import { connect } from 'react-redux';
import { NavLink, useHistory } from 'react-router-dom';
import * as actions from '../store/actions/auth';
import '../style.css';
import { Spin } from 'antd';

const NormalLoginForm = (props) => {
  const [form] = Form.useForm();
  const history = useHistory();

  const handleSubmit = async (values) => {
    try {
      await props.onAuth(values.username, values.password);
      history.push('/');
    } catch (error) {
      console.error(error);
    }
  };

  let errorMessage = null;
  if (props.error) {
    errorMessage = <p>{props.error.message}</p>;
  }

  return (
    <div>
      {errorMessage}
      {props.loading ? (
        <Spin />
      ) : (
        <Form form={form} onFinish={handleSubmit} className="login-form">
          <Form.Item name="username" rules={[{ required: true, message: 'Please input your username!' }]}>
            <Input placeholder="Username" />
          </Form.Item>
          <Form.Item name="password" rules={[{ required: true, message: 'Please input your Password!' }]}>
            <Input type="password" placeholder="Password" />
          </Form.Item>
          <Form.Item>
            <Button type="primary" htmlType="submit" style={{ marginRight: '10px' }}>
              Login
            </Button>
            Or
            <NavLink style={{ marginRight: '10px' }} to="/register/">
              Register
            </NavLink>
          </Form.Item>
        </Form>
      )}
    </div>
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
    onAuth: (username, password) => dispatch(actions.authLogin(username, password)),
  };
};

export default connect(mapStateToProps, mapDispatchToProps)(NormalLoginForm);