class ModifyElement {
    constructor() {
        return this
    }
    static replicateElement(element, nth, parentElement) {
        const body = document.body
        let clonedElements = new Array()
        for (let i = 0; i < nth; i++) {
            const clonedElement = element.cloneNode(true)
            clonedElements.push(clonedElement)
            if (parentElement) {
                parentElement.appendChild(clonedElement)
            }
            else {
                body.appendChild(clonedElement)
            }
        }
        return clonedElements
    }
}