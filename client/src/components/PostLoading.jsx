import React from 'react'

function PostLoading(Component) {
  return function PostLoadingComponent({isLoading, ...props}) {
    if (isLoading === false) return <Component props={props} />
    return (
        <h1>WOAH</h1>
    )
  }
}

export default PostLoading