import Konva from 'konva'

const CANVAS_WIDTH = 1000
const CANVAS_HEIGHT = 650

const stage = new Konva.Stage({
  container: 'tree',
  width: CANVAS_WIDTH,
  height: CANVAS_HEIGHT,
  draggable: true,
})

const layer = new Konva.Layer()
stage.add(layer)

const nodeTemplate = (document.querySelector('#node-tmpl') as HTMLDivElement);
const nodeStyles = getComputedStyle(nodeTemplate);

const PADDING_TOP = 20
const PADDING_INNER = 60

const nodeProps = {
  radius: 30,
  fill: nodeStyles.getPropertyValue('background-color')
}

const xR = CANVAS_WIDTH / 2
const yR = nodeProps.radius + PADDING_TOP
const xA = CANVAS_WIDTH / 4
const yA = nodeProps.radius * 2 + PADDING_TOP + PADDING_INNER
const xA1 = CANVAS_WIDTH / 8
const yA1 = nodeProps.radius * 4 + PADDING_TOP + PADDING_INNER * 2
const xA2 = CANVAS_WIDTH / 8 * 3
const xB = CANVAS_WIDTH / 4 * 3
const xB1 = CANVAS_WIDTH / 8 * 5
const xB2 = CANVAS_WIDTH / 8 * 7

const nodePositions = {
  'R': [xR, yR, xR, yR],
  'A': [xR, yR, xA, yA],
  'A1': [xA, yA, xA1, yA1],
  'A2': [xA, yA, xA2, yA1],
  'B': [xR, yR, xB, yA],
  'B1': [xB, yA, xB1, yA1],
  'B2': [xB, yA, xB2, yA1],
};

export function setupVis() {
  const nodeGroups: Record<string, Konva.Group> = {}
  const textos: Record<string, Konva.Text> = {}
  for (const n of Object.keys(nodePositions).reverse()) {
    const group = new Konva.Group()
    nodeGroups[n] = group
    const line = new Konva.Line({
      points: nodePositions[n as keyof typeof nodePositions],
      stroke: nodeProps.fill,
    })
    const circle = new Konva.Circle({
      x: nodePositions[n as keyof typeof nodePositions][2],
      y: nodePositions[n as keyof typeof nodePositions][3],
      ...nodeProps,
    })
    const text = new Konva.Text({
      text: "teste",
      x: nodePositions[n as keyof typeof nodePositions][2],
      y: nodePositions[n as keyof typeof nodePositions][3],
      fill: nodeStyles.getPropertyValue("color"),
      width: nodeProps.radius * 2,
      align: 'center'
    })
    group.add(circle)
    group.add(text)
    group.add(line)
    line.setZIndex(0)
    text.setZIndex(2)
    group.visible(false)
    layer.add(group)
    textos[n] = text
  }
  layer.batchDraw()

  return [nodeGroups, textos] as const
}
