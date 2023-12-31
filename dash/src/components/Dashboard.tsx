import React from 'react';
import "../styles/Dashboard.css";
import RequestChart from './RequestChart';
import SimpleBarChart from './SimpleBarChart';

const Dashboard: React.FC = () => {

    return(
        <div className="dashboard-container">
            <div className="dashboard-container-col-1">
                <div className="board-1-container">
                    <RequestChart></RequestChart>                    
                </div>
                <div className="board-2-container">
                    <SimpleBarChart></SimpleBarChart>
                </div>
            </div>
            <div className="dashboard-container-col-2">
                <div className="board-3-container">
                    This will be the query explorer
                </div>
            </div>
        </div>
    );
}

export default Dashboard;