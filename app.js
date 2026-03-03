function validateName(name) {
  return name && name.trim() !== ''
}

function runApp() {
  const name = 'Sample User'

  if (validateName(name)) {
    console.log('Hello, ' + name)
  } else {
    console.log('Invalid name')
  }
}

runApp()
