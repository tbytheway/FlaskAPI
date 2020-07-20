import React,  { Component } from 'react'

import App from './app'

export default class RenderMovies extends Component {
    render(props) {
        return (
            <div className="movie">
                <div>Title: {this.props.title}</div>
                <div>actors: {this.props.actors}</div>
            </div>
        )
    }
}