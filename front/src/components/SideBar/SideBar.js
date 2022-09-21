import React from 'react';
import styled from 'styled-components';

const StyledNav = styled.nav`
  position: fixed;
  top: 0;
  left: 0;
  width: 5vw;
  height: 100%;
  background: linear-gradient(45deg, #5887BF 30%, #86BFC9 90%);
  margin-right: 20px;
`;

/**
 サイドバーの分だけpaddingを持たせる
 */
const StyledUL = styled.ul`
  padding: 5vw;
`;

export default function Nav() {
  return(
    <StyledNav>
      <StyledUL>
      {// <li>種族値クイズ</li>
      }
      </StyledUL>
    </StyledNav>
  );
}