import React from 'react';
import { Route } from 'react-router-dom'

import BurstList from './containers/BurstListView';
import BurstDetail from './containers/BurstDetailView';
import Login from './containers/Login';
import Register from './containers/Register';

const BaseRouter = () => (
    <div>
        <Route exact path='/' component={BurstList} />
        <Route exact path='/bursts/:burstID' component={BurstDetail} />
        <Route exact path='/login/' component={Login} />
        <Route exact path='/register/' component={Register} />
    </div>

);

export default BaseRouter;