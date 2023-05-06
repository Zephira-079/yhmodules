class ScrollResponse {
  constructor() {
    return this
  }

  //recommended to use for now!!! absoluteRectAll
  static absoluteRectAll(querySelector) {
    const elements = document.querySelectorAll(querySelector)
    const offsets = []
    elements.forEach(element => {
      let offset = { element: element, top: 0, left: 0, right: 0, bottom: 0, width: 0, height: 0, originX: 0, originY: 0 }
      const rect = element.getBoundingClientRect()
      offset.top = rect.top
      offset.left = rect.left
      offset.right = rect.right
      offset.bottom = rect.bottom
      offset.width = rect.width
      offset.height = rect.height
      offset.originX = rect.left + ((rect.right - rect.left) / 2) // rect.left + (rect.width / 2)
      offset.originY = rect.top + ((rect.bottom - rect.top) / 2) // rect.top + (rect.height / 2)

      offsets.push(offset)
    })
    return offsets
  }
  static paralax
}