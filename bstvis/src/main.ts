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

  const divInfo = document.querySelector('#tree-info') as HTMLDivElement
  divInfo.innerHTML =
`<strong>Altura</strong> ${bst.height()}; <strong>Comprimento</strong> ${bst.internalPathLength()}; <Strong>Tamanho</Strong> ${bst.size()};
<br><strong>Mínimo</strong> ${bst.min() || "---"}; <strong>Máximo</strong> ${bst.max() || "---"}`
}

const getInputEntry = () => document.querySelector('#inpen') as HTMLInputElement

function onClickAdd() {
  const valor = parseInt(getInputEntry()?.value)
  if (valor === 0 || valor) {
    bst.push(valor)
  }
  updateVis()
}

let lastTimer: number | undefined = undefined

function onClickFind() {
  const valor = parseInt(getInputEntry()?.value)
  if (!valor && valor !== 0) {
    return
  }
  const divRes = document.querySelector('#skb-fnd') as HTMLDivElement
  if (bst.find(valor)) {
    divRes.innerText = `✅ Elemento ${valor} encontrado.`
    divRes.showPopover()
  } else {
    divRes.innerText = `❌ Elemento ${valor} NÃO encontrado.`
    divRes.showPopover()
  }
  document.body.appendChild(divRes)
  if (lastTimer !== undefined) {
    clearTimeout(lastTimer)
  }
  lastTimer = setTimeout(() => divRes.hidePopover(), 3000)
}

function onClickPercorrer() {
  const dlgPercorrer = document.querySelector('#dlg-pcr') as HTMLDialogElement
  dlgPercorrer.innerHTML = `
<strong>Pre-Ordem</strong>: ${bst.preOrdem()}<br>
<strong>Pos-Ordem</strong>: ${bst.posOrdem()}<br>
<strong>Em-Ordem</strong>: ${bst.emOrdem()}<br>
<strong>Nível-Ordem</strong>: ${bst.levelOrder()}<br>
`
}

updateVis();

(document.querySelector('#btn-add') as HTMLButtonElement)?.addEventListener('click', onClickAdd);
(document.querySelector('#btn-fnd') as HTMLButtonElement)?.addEventListener('click', onClickFind);
(document.querySelector('#btn-pcr') as HTMLButtonElement)?.addEventListener('click', onClickPercorrer);
getInputEntry().addEventListener('keydown', (e: KeyboardEvent) => e.key == "Enter" && onClickAdd())
