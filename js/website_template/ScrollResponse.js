class ScrollResponse {
  constructor() {
    return this
  }

  //recommended to use for now!!! absoluteRectAll
  static absoluteRectAll(querySelector) {
    const elements = document.querySelectorAll(querySelector)
    const offsets = []
    elements.forEach(element => {
      let offset = {element: element, top: 0, left: 0, right: 0, bottom: 0, width: 0, height: 0}
      const rect = element.getBoundingClientRect()
      offset.top = rect.top
      offset.left = rect.left
      offset.right = rect.right
      offset.bottom = rect.bottom
      offset.width = rect.width
      offset.height = rect.height
      
      offsets.push(offset)
    })
    return offsets
  }
}
