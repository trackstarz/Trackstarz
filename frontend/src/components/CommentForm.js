import React from 'react';
import { Form, Input, Button } from 'antd';
import { connect } from 'react-redux';
import axios from 'axios';

class CommentForm extends React.Component {
  handleFormSubmit = (event, requestType, commentID, burstID) => {
    event.preventDefault();
    const content = event.target.elements.content.value;
    const author = this.props.user?.id; // or replace with the correct user object from state
    axios.defaults.headers = {
      'Content-Type': 'application/json',
      Authorization: this.props.token,
    };
    switch (requestType) {
      case 'post':
        return axios
          .post('http://34.222.26.155:8080/api/comments/', {
            author: author,
            content: content,
            burst: burstID,
          })
          .then((res) => console.log(res))
          .catch((error) => console.error(error));
      case 'put':
        return axios
          .put(`http://34.222.26.155:8080/api/comments/${commentID}/`, {
            author: author,
            content: content,
            burst: burstID,
          })
          .then((res) => console.log(res))
          .catch((error) => console.error(error));
      default:
        return null;
    }
  };

  render() {
    return (
      <div>
        <Form
          className="burst_inputs"
          id="comment_form"
          onSubmit={(event) =>
            this.handleFormSubmit(
              event,
              this.props.requestType,
              this.props.commentID,
              this.props.burstID
            )
          }
        >
          <Form.Item>
            <Input name="content" placeholder="Tell us what is going on..." />
          </Form.Item>
          <Form.Item>
            <Button
              id="burst_submit"
              type="primary"
              htmlType="submit"
            >
              {this.props.btnText}
            </Button>
          </Form.Item>
        </Form>
      </div>
    );
  }
}

const mapStateToProps = (state) => {
  return {
    token: state.token,
    user: state.user,
  };
};

export default connect(mapStateToProps)(CommentForm);
