DEFI_SDK_ROUTER_ABI = [
    {
        'inputs': [
            {
                'internalType': 'address payable',
                'name': 'core',
                'type': 'address'
            }
        ],
        'stateMutability': 'nonpayable',
        'type': 'constructor'
    },
    {
        'anonymous': 'false',
        'inputs': [
            {
                'indexed': 'true',
                'internalType': 'address',
                'name': 'previousOwner',
                'type': 'address'
            },
            {
                'indexed': 'true',
                'internalType': 'address',
                'name': 'newOwner',
                'type': 'address'
            }
        ],
        'name': 'OwnershipTransferred',
        'type': 'event'
    },
    {
        'inputs': [

        ],
        'name': 'acceptOwnership',
        'outputs': [

        ],
        'stateMutability': 'nonpayable',
        'type': 'function'
    },
    {
        'inputs': [

        ],
        'name': 'core',
        'outputs': [
            {
                'internalType': 'address',
                'name': '',
                'type': 'address'
            }
        ],
        'stateMutability': 'view',
        'type': 'function'
    },
    {
        'inputs': [
            {
                'components': [
                    {
                        'components': [
                            {
                                'internalType': 'bytes32',
                                'name': 'protocolAdapterName',
                                'type': 'bytes32'
                            },
                            {
                                'internalType': 'enum ActionType',
                                'name': 'actionType',
                                'type': 'uint8'
                            },
                            {
                                'components': [
                                    {
                                        'internalType': 'address',
                                        'name': 'token',
                                        'type': 'address'
                                    },
                                    {
                                        'internalType': 'uint256',
                                        'name': 'amount',
                                        'type': 'uint256'
                                    },
                                    {
                                        'internalType': 'enum AmountType',
                                        'name': 'amountType',
                                        'type': 'uint8'
                                    }
                                ],
                                'internalType': 'struct TokenAmount[]',
                                'name': 'tokenAmounts',
                                'type': 'tuple[]'
                            },
                            {
                                'internalType': 'bytes',
                                'name': 'data',
                                'type': 'bytes'
                            }
                        ],
                        'internalType': 'struct Action[]',
                        'name': 'actions',
                        'type': 'tuple[]'
                    },
                    {
                        'components': [
                            {
                                'internalType': 'address',
                                'name': 'token',
                                'type': 'address'
                            },
                            {
                                'internalType': 'uint256',
                                'name': 'amount',
                                'type': 'uint256'
                            },
                            {
                                'internalType': 'enum AmountType',
                                'name': 'amountType',
                                'type': 'uint8'
                            }
                        ],
                        'internalType': 'struct TokenAmount[]',
                        'name': 'inputs',
                        'type': 'tuple[]'
                    },
                    {
                        'components': [
                            {
                                'internalType': 'uint256',
                                'name': 'share',
                                'type': 'uint256'
                            },
                            {
                                'internalType': 'address',
                                'name': 'beneficiary',
                                'type': 'address'
                            }
                        ],
                        'internalType': 'struct Fee',
                        'name': 'fee',
                        'type': 'tuple'
                    },
                    {
                        'components': [
                            {
                                'internalType': 'address',
                                'name': 'token',
                                'type': 'address'
                            },
                            {
                                'internalType': 'uint256',
                                'name': 'amount',
                                'type': 'uint256'
                            }
                        ],
                        'internalType': 'struct AbsoluteTokenAmount[]',
                        'name': 'requiredOutputs',
                        'type': 'tuple[]'
                    },
                    {
                        'internalType': 'uint256',
                        'name': 'nonce',
                        'type': 'uint256'
                    }
                ],
                'internalType': 'struct TransactionData',
                'name': 'data',
                'type': 'tuple'
            },
            {
                'internalType': 'bytes',
                'name': 'signature',
                'type': 'bytes'
            }
        ],
        'name': 'getAccountFromSignature',
        'outputs': [
            {
                'internalType': 'address payable',
                'name': '',
                'type': 'address'
            }
        ],
        'stateMutability': 'view',
        'type': 'function'
    },
    {
        'inputs': [
            {
                'components': [
                    {
                        'internalType': 'address',
                        'name': 'token',
                        'type': 'address'
                    },
                    {
                        'internalType': 'uint256',
                        'name': 'amount',
                        'type': 'uint256'
                    },
                    {
                        'internalType': 'enum AmountType',
                        'name': 'amountType',
                        'type': 'uint8'
                    }
                ],
                'internalType': 'struct TokenAmount[]',
                'name': 'inputs',
                'type': 'tuple[]'
            },
            {
                'internalType': 'address',
                'name': 'account',
                'type': 'address'
            }
        ],
        'name': 'getRequiredAllowances',
        'outputs': [
            {
                'components': [
                    {
                        'internalType': 'address',
                        'name': 'token',
                        'type': 'address'
                    },
                    {
                        'internalType': 'uint256',
                        'name': 'amount',
                        'type': 'uint256'
                    }
                ],
                'internalType': 'struct AbsoluteTokenAmount[]',
                'name': '',
                'type': 'tuple[]'
            }
        ],
        'stateMutability': 'view',
        'type': 'function'
    },
    {
        'inputs': [
            {
                'components': [
                    {
                        'internalType': 'address',
                        'name': 'token',
                        'type': 'address'
                    },
                    {
                        'internalType': 'uint256',
                        'name': 'amount',
                        'type': 'uint256'
                    },
                    {
                        'internalType': 'enum AmountType',
                        'name': 'amountType',
                        'type': 'uint8'
                    }
                ],
                'internalType': 'struct TokenAmount[]',
                'name': 'inputs',
                'type': 'tuple[]'
            },
            {
                'internalType': 'address',
                'name': 'account',
                'type': 'address'
            }
        ],
        'name': 'getRequiredBalances',
        'outputs': [
            {
                'components': [
                    {
                        'internalType': 'address',
                        'name': 'token',
                        'type': 'address'
                    },
                    {
                        'internalType': 'uint256',
                        'name': 'amount',
                        'type': 'uint256'
                    }
                ],
                'internalType': 'struct AbsoluteTokenAmount[]',
                'name': '',
                'type': 'tuple[]'
            }
        ],
        'stateMutability': 'view',
        'type': 'function'
    },
    {
        'inputs': [
            {
                'internalType': 'address',
                'name': 'account',
                'type': 'address'
            }
        ],
        'name': 'nonce',
        'outputs': [
            {
                'internalType': 'uint256',
                'name': '',
                'type': 'uint256'
            }
        ],
        'stateMutability': 'view',
        'type': 'function'
    },
    {
        'inputs': [

        ],
        'name': 'owner',
        'outputs': [
            {
                'internalType': 'address',
                'name': '',
                'type': 'address'
            }
        ],
        'stateMutability': 'view',
        'type': 'function'
    },
    {
        'inputs': [

        ],
        'name': 'pendingOwner',
        'outputs': [
            {
                'internalType': 'address',
                'name': '',
                'type': 'address'
            }
        ],
        'stateMutability': 'view',
        'type': 'function'
    },
    {
        'inputs': [
            {
                'internalType': 'address',
                'name': 'newOwner',
                'type': 'address'
            }
        ],
        'name': 'proposeOwnership',
        'outputs': [

        ],
        'stateMutability': 'nonpayable',
        'type': 'function'
    },
    {
        'inputs': [
            {
                'internalType': 'address',
                'name': 'token',
                'type': 'address'
            },
            {
                'internalType': 'address payable',
                'name': 'beneficiary',
                'type': 'address'
            }
        ],
        'name': 'returnLostTokens',
        'outputs': [

        ],
        'stateMutability': 'nonpayable',
        'type': 'function'
    },
    {
        'inputs': [
            {
                'components': [
                    {
                        'internalType': 'bytes32',
                        'name': 'protocolAdapterName',
                        'type': 'bytes32'
                    },
                    {
                        'internalType': 'enum ActionType',
                        'name': 'actionType',
                        'type': 'uint8'
                    },
                    {
                        'components': [
                            {
                                'internalType': 'address',
                                'name': 'token',
                                'type': 'address'
                            },
                            {
                                'internalType': 'uint256',
                                'name': 'amount',
                                'type': 'uint256'
                            },
                            {
                                'internalType': 'enum AmountType',
                                'name': 'amountType',
                                'type': 'uint8'
                            }
                        ],
                        'internalType': 'struct TokenAmount[]',
                        'name': 'tokenAmounts',
                        'type': 'tuple[]'
                    },
                    {
                        'internalType': 'bytes',
                        'name': 'data',
                        'type': 'bytes'
                    }
                ],
                'internalType': 'struct Action[]',
                'name': 'actions',
                'type': 'tuple[]'
            },
            {
                'components': [
                    {
                        'internalType': 'address',
                        'name': 'token',
                        'type': 'address'
                    },
                    {
                        'internalType': 'uint256',
                        'name': 'amount',
                        'type': 'uint256'
                    },
                    {
                        'internalType': 'enum AmountType',
                        'name': 'amountType',
                        'type': 'uint8'
                    }
                ],
                'internalType': 'struct TokenAmount[]',
                'name': 'inputs',
                'type': 'tuple[]'
            },
            {
                'components': [
                    {
                        'internalType': 'uint256',
                        'name': 'share',
                        'type': 'uint256'
                    },
                    {
                        'internalType': 'address',
                        'name': 'beneficiary',
                        'type': 'address'
                    }
                ],
                'internalType': 'struct Fee',
                'name': 'fee',
                'type': 'tuple'
            },
            {
                'components': [
                    {
                        'internalType': 'address',
                        'name': 'token',
                        'type': 'address'
                    },
                    {
                        'internalType': 'uint256',
                        'name': 'amount',
                        'type': 'uint256'
                    }
                ],
                'internalType': 'struct AbsoluteTokenAmount[]',
                'name': 'requiredOutputs',
                'type': 'tuple[]'
            }
        ],
        'name': 'startExecution',
        'outputs': [
            {
                'components': [
                    {
                        'internalType': 'address',
                        'name': 'token',
                        'type': 'address'
                    },
                    {
                        'internalType': 'uint256',
                        'name': 'amount',
                        'type': 'uint256'
                    }
                ],
                'internalType': 'struct AbsoluteTokenAmount[]',
                'name': '',
                'type': 'tuple[]'
            }
        ],
        'stateMutability': 'payable',
        'type': 'function'
    },
    {
        'inputs': [
            {
                'components': [
                    {
                        'components': [
                            {
                                'internalType': 'bytes32',
                                'name': 'protocolAdapterName',
                                'type': 'bytes32'
                            },
                            {
                                'internalType': 'enum ActionType',
                                'name': 'actionType',
                                'type': 'uint8'
                            },
                            {
                                'components': [
                                    {
                                        'internalType': 'address',
                                        'name': 'token',
                                        'type': 'address'
                                    },
                                    {
                                        'internalType': 'uint256',
                                        'name': 'amount',
                                        'type': 'uint256'
                                    },
                                    {
                                        'internalType': 'enum AmountType',
                                        'name': 'amountType',
                                        'type': 'uint8'
                                    }
                                ],
                                'internalType': 'struct TokenAmount[]',
                                'name': 'tokenAmounts',
                                'type': 'tuple[]'
                            },
                            {
                                'internalType': 'bytes',
                                'name': 'data',
                                'type': 'bytes'
                            }
                        ],
                        'internalType': 'struct Action[]',
                        'name': 'actions',
                        'type': 'tuple[]'
                    },
                    {
                        'components': [
                            {
                                'internalType': 'address',
                                'name': 'token',
                                'type': 'address'
                            },
                            {
                                'internalType': 'uint256',
                                'name': 'amount',
                                'type': 'uint256'
                            },
                            {
                                'internalType': 'enum AmountType',
                                'name': 'amountType',
                                'type': 'uint8'
                            }
                        ],
                        'internalType': 'struct TokenAmount[]',
                        'name': 'inputs',
                        'type': 'tuple[]'
                    },
                    {
                        'components': [
                            {
                                'internalType': 'uint256',
                                'name': 'share',
                                'type': 'uint256'
                            },
                            {
                                'internalType': 'address',
                                'name': 'beneficiary',
                                'type': 'address'
                            }
                        ],
                        'internalType': 'struct Fee',
                        'name': 'fee',
                        'type': 'tuple'
                    },
                    {
                        'components': [
                            {
                                'internalType': 'address',
                                'name': 'token',
                                'type': 'address'
                            },
                            {
                                'internalType': 'uint256',
                                'name': 'amount',
                                'type': 'uint256'
                            }
                        ],
                        'internalType': 'struct AbsoluteTokenAmount[]',
                        'name': 'requiredOutputs',
                        'type': 'tuple[]'
                    },
                    {
                        'internalType': 'uint256',
                        'name': 'nonce',
                        'type': 'uint256'
                    }
                ],
                'internalType': 'struct TransactionData',
                'name': 'data',
                'type': 'tuple'
            },
            {
                'internalType': 'bytes',
                'name': 'signature',
                'type': 'bytes'
            }
        ],
        'name': 'startExecution',
        'outputs': [
            {
                'components': [
                    {
                        'internalType': 'address',
                        'name': 'token',
                        'type': 'address'
                    },
                    {
                        'internalType': 'uint256',
                        'name': 'amount',
                        'type': 'uint256'
                    }
                ],
                'internalType': 'struct AbsoluteTokenAmount[]',
                'name': '',
                'type': 'tuple[]'
            }
        ],
        'stateMutability': 'payable',
        'type': 'function'
    }
]
