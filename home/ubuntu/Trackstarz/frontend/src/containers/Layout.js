import React from 'react';
import { Layout, Menu } from 'antd';
import * as actions from '../store/actions/auth';
import { connect } from 'react-redux';
import { Link, withRouter }  from 'react-router-dom'

const { Header, Content, Footer, Sider} = Layout;

class CustomLayout extends React.Component {
  render() {

    return (

      <Layout className="layout">
        <Header className="header">
          <div className="logo" />
          <Menu
            theme="dark"
            mode="horizontal"
            defaultSelectedKeys={['1']}
            style={{ lineHeight: '64px' }}
          >
          <Menu.Item key="1"><Link to="/">Home</Link></Menu.Item>
          {
            this.props.isAuthenticated ?
  
            <Menu.Item key="2" onClick={this.props.logout}>
              Logout
            </Menu.Item>
          
          
          :
  
          <Menu.Item key="2"><Link to="/login">Login</Link></Menu.Item>
        }
            
          </Menu>
        </Header>
        <Layout>
          <div style={{ background: '#fff', minHeight: 400 }}>
  
          </div>
  
        </Layout>
        <Layout style={{padding: '20px 50px 0px 50px'}}>
          <Sider width={300} style={{ background: '#f0f2f5', padding: '0 50px' }}>
          <div style={{ padding: 24, minHeight: 280 }}>
               
              </div>
          </Sider>
          <Content width={600} style={{ padding: '0 50px' }}>
              <div style={{ padding: 24, minHeight: 280 }}>
                {this.props.children}
              </div>
          </Content>
          <Sider width={300} style={{ background: '#f0f2f5', padding: '0 50px' }}>
          <div style={{ padding: 24, minHeight: 280 }}>
                
              </div>
          </Sider>
        </Layout>
        <Footer style={{ textAlign: 'center' }}>Trackstarz ©2019</Footer>
      </Layout>
  
    );
  }

  }
  
 

    const mapDispatchToProps = dispatch => {
        return {
            logout: () => dispatch(actions.logout())
        }
    }

    export default withRouter(connect(null, mapDispatchToProps)(CustomLayout));


