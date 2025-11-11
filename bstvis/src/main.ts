import "./style.css"

import { BST } from './bst'
import { setupVis } from './visualiser'

const bst = new BST();

const [nodeGroups, textos] = setupVis()

function updateText(n: string, val: number) {
  textos[n].setText(val?.toString())
  textos[n].offsetX(textos[n].width() / 2)
  textos[n].offsetY(textos[n].height() / 2)
}

function updateVis() {
  nodeGroups['R'].visible(false)

  nodeGroups['A'].visible(false)
  nodeGroups['A1'].visible(false)
  nodeGroups['A2'].visible(false)

  nodeGroups['B'].visible(false)
  nodeGroups['B1'].visible(false)
  nodeGroups['B2'].visible(false)

  if (bst.root !== undefined) {
    updateText('R', bst.root.value)
    nodeGroups['R'].visible(true)
    if (bst.root.left !== undefined) {
      updateText('A', bst.root.left.value)
      nodeGroups['A'].visible(true)
      if (bst.root.left.left !== undefined) {
        updateText('A1', bst.root.left.left.value)
        nodeGroups['A1'].visible(true)
      }
      if (bst.root.left.right !== undefined) {
        updateText('A2', bst.root.left.right.value)
        nodeGroups['A2'].visible(true)
      }
    }
    if (bst.root.right !== undefined) {
      updateText('B', bst.root.right.value)
      nodeGroups['B'].visible(true)
      if (bst.root.right.left !== undefined) {
        updateText('B1', bst.root.right.left.value)
        nodeGroups['B1'].visible(true)
      }
      if (bst.root.right.right !== undefined) {
        updateText('B2', bst.root.right.right.value)
        nodeGroups['B2'].visible(true)
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
