import { Radio } from 'antd';
import {
  EmissionsTargetValue,
  useEmissionsTarget,
} from 'pages/Wells/pages/WellPlanning/containers/EmissionsTargetProvider';

const EmissionsTargetSwitch = () => {
  const [
    {
      value,
      scopes: { scope1, scope2, scope3 },
    },
    dispatch,
  ] = useEmissionsTarget();
  const isLastActiveScope =
    [scope1, scope2, scope3].filter(Boolean).length === 1;

  return (
    <Radio.Group
      buttonStyle="solid"
      onChange={(event) =>
        dispatch({
          type: 'changeValue',
          value: event.target.value,
        })
      }
      defaultValue={value}
    >
      <Radio.Button value={EmissionsTargetValue.CO2}>
        CO
        <sub>2</sub>
      </Radio.Button>
      <Radio.Button value={EmissionsTargetValue.NOx}>NOx</Radio.Button>
      <Radio.Button
        value={EmissionsTargetValue.Fuel}
        disabled={isLastActiveScope && scope2}
      >
        Fuel
      </Radio.Button>
      <Radio.Button
        value={EmissionsTargetValue.FuelCost}
        disabled={isLastActiveScope && scope2}
      >
        Fuel cost
      </Radio.Button>
    </Radio.Group>
  );
};

export default EmissionsTargetSwitch;
