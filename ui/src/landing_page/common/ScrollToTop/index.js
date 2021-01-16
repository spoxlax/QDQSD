import React from "react";
import { BackTop } from "antd";
import SvgIcon from "../SvgIcon";

import * as S from "./styles";

const Input = () => (
  <BackTop>
    <S.Up>
      <SvgIcon src="scroll-top.svg" />
    </S.Up>
  </BackTop>
);

export default Input;
