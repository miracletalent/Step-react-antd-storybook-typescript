import { Flexbox } from 'components/Box';
import { Text } from 'components/Typography';
import { prettyNumber, roundNumber } from 'utils/format';

interface TooltipItemProps {
  title: string;
  value: number;
  unit: React.ReactNode;
}

const TooltipItem = ({ title, value, unit }: TooltipItemProps) => {
  return (
    <Flexbox gap={6} alignItems="center">
      <Flexbox justifyContent="flex-start" flexGrow={1}>
        <Text fontSize={8} lineHeight="16px">
          {title}
        </Text>
      </Flexbox>
      <Flexbox justifyContent="flex-end" flexGrow={1}>
        <Text fontSize={8} lineHeight="16px">
          {prettyNumber(roundNumber(value, 2))} {unit}
        </Text>
      </Flexbox>
    </Flexbox>
  );
};

export default TooltipItem;
