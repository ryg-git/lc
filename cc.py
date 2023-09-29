class TreeNode:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.val = data

    def PrintTree(self):
        print(self.val)


def poTravel(tn: TreeNode):
    st, po = [], []

    current = tn

    lv = None

    ls, rs = [[0, 0]], []

    while st or current:
        if current:
            st.append(current)
            current = current.left
            if current:
                if rs and rs[-1][0] > ls[-1][0]:
                    ls.append([rs[-1][0] + 1 if rs else 1, 0])
                else:
                    ls.append([ls[-1][0] + 1 if ls else 1, 0])

        else:
            if st[-1].right and lv != st[-1].right:
                current = st[-1].right
                if rs and ls[-1][0] > rs[-1][0]:
                    rs.append([ls[-1][0] + 1 if ls else 1, 0])
                elif not rs and ls:
                    rs.append([ls[-1][0] + 1 if ls else 1, 0])
                else:
                    rs.append([rs[-1][0] + 1 if rs else 1, 0])

            else:
                nd = st.pop()

                if not rs and ls:
                    nv = ls[-1][1] + nd.val
                    po.append(nv)
                    ls.pop()
                    if ls:
                        ls[-1][1] += nv

                elif not ls and rs:
                    nv = rs[-1][1] + nd.val
                    po.append(nv)
                    rs.pop()
                    if rs:
                        rs[-1][1] += nv

                elif ls[-1][0] < rs[-1][0]:
                    nv = rs[-1][1] + nd.val
                    po.append(nv)
                    rs.pop()
                    if rs and ls[-1][0] < rs[-1][0]:
                        rs[-1][1] += nv
                    else:
                        ls[-1][1] += nv

                elif rs[-1][0] < ls[-1][0]:
                    nv = ls[-1][1] + nd.val
                    po.append(nv)
                    ls.pop()
                    if ls and rs[-1][0] < ls[-1][0]:
                        ls[-1][1] += nv
                    else:
                        rs[-1][1] += nv

                lv = nd

    return po


def main():
    r = TreeNode(7)
    r.left = TreeNode(3)
    r.left.left = TreeNode(6)
    # r.left.left = TreeNode(1)
    r.left.left.left = TreeNode(2)
    r.left.left.left.left = TreeNode(4)
    r.right = TreeNode(5)

    poTravel(r)


main()
