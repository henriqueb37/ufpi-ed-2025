import "./style.css"

console.debug('Hello, world!')
console.debug('Help me not')

class Node {
  value: number;
  left: Node | undefined;
  right: Node | undefined;

  constructor(value: number) {
    this.value = value;
  }

  insert(value: number): undefined {
    if (this.value == value) {
      return;
    }
    if (value < this.value) {
      if (this.left !== undefined) {
        return this.left.insert(value);
      }
      this.left = new Node(value);
    } else {
      if (this.right !== undefined) {
        return this.right.insert(value);
      }
      this.right = new Node(value);
    }
  }
}

class BST {
  root: Node | undefined;

  constructor() {
    
  }

  push(value: number) {
    if (this.root == undefined) {
      this.root = new Node(value);
    }
    this.root.insert(value);
  }
}

function getNodeDiv(selector: string): HTMLDivElement {
  return (document.querySelector(selector) as HTMLDivElement)
}

const bst = new BST();

const nodeR = getNodeDiv('#node-r')

const nodeA  = getNodeDiv('#node-a')
const nodeA1 = getNodeDiv('#node-a1')
const nodeA2 = getNodeDiv('#node-a2')

const nodeB  = getNodeDiv('#node-b')
const nodeB1 = getNodeDiv('#node-b1')
const nodeB2 = getNodeDiv('#node-b2')

function updateVis() {
  nodeR.style.visibility = "hidden"

  nodeA.style.visibility = "hidden"
  nodeA1.style.visibility = "hidden"
  nodeA2.style.visibility = "hidden"

  nodeB.style.visibility = "hidden"
  nodeB1.style.visibility = "hidden"
  nodeB2.style.visibility = "hidden"

  if (bst.root !== undefined) {
    nodeR.innerText = bst.root.value.toString()
    nodeR.style.visibility = "visible"
    if (bst.root.left !== undefined) {
      nodeA.innerText = bst.root.left.value.toString()
      nodeA.style.visibility = "visible"
      if (bst.root.left.left !== undefined) {
        nodeA1.innerText = bst.root.left.left.value.toString()
        nodeA1.style.visibility = "visible"
      }
      if (bst.root.left.right !== undefined) {
        nodeA2.innerText = bst.root.left.right.value.toString()
        nodeA2.style.visibility = "visible"
      }
    }
    if (bst.root.right !== undefined) {
      nodeB.innerText = bst.root.right.value.toString()
      nodeB.style.visibility = "visible"
      if (bst.root.right.left !== undefined) {
        nodeB1.innerText = bst.root.right.left.value.toString()
        nodeB1.style.visibility = "visible"
      }
      if (bst.root.right.right !== undefined) {
        nodeB2.innerText = bst.root.right.right.value.toString()
        nodeB2.style.visibility = "visible"
      }
    }
  }
}

function onClickAdd() {
  const valor = parseInt((document.querySelector('#inpen') as HTMLInputElement)?.value)
  if (valor === 0 || valor) {
    bst.push(valor)
  }
  updateVis()
}

updateVis();

(document.querySelector('#btn-add') as HTMLButtonElement)?.addEventListener('click', onClickAdd)
